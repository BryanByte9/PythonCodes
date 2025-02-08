from datetime import datetime
def menu():
    choice=int(input("""You may select one of the following:
1) List available cars
2) Rent a car
3) Return a car
4) Count the money
0) Exit
What is your selection?\n"""))
    return choice

def get_list(cars_file,rented_file):
    #to get the list "rented_cars,available_cars" needed for rent & return
    data = []  # Stores the data of "available cars"
    file = open(cars_file, 'r')
    lines = file.read().splitlines()
    file.close()

    # split the line in lines by ",",then add them in data
    for line in lines:
        component = line.split(",")
        data.append(component)

    rented_file = open(rented_file, 'r')
    rented_lines = rented_file.read().splitlines()
    rented_file.close()

    # add rented cars' plate number in the list
    rented_cars = []
    for line in rented_lines:
        rented_plate = line.split(",")[0]
        rented_cars.append(rented_plate)

    #add available cars' all info in the matrix
    available_cars = []
    for car in data:
        if car[0] not in rented_cars:
            available_cars.append(car)

    return available_cars, rented_cars


def list_available(cars_file,rented_file):

    available_cars, rented_cars = get_list(cars_file, rented_file)

    for car in available_cars:
        reg_nr = car[0]
        model = car[1]
        price_per_day = car[2]
        print(f"* Reg. nr: {reg_nr}, Model: {model}, Price per day: {price_per_day}")
        #print properties of the car using loop
        properties = ""
        for i in range (3,len(car)):
            if i == len(car)-1:#no comma on the last property
                properties = properties + car[i]
            else:
                properties = properties + car[i] + ", "
        print(f"Properties: {properties}")
    print("")

def rent_a_car(cars_file,rented_file):

    available_cars, rented_cars = get_list(cars_file, rented_file)

    plate_number=input("Give the register number of the car you want to rent:\n")
    #check if the car has been rented
    for rented_car in rented_cars:
        if plate_number in rented_car:
            print(f"{rented_car} already rented\n")
            return#exit this function, go back to menu
        
    #check if the car exists, if not go back to menu
    car_exist = False
    for car in available_cars:
        if car[0] == plate_number:
            car_exist = True
            break

    if not car_exist:
        print("Car does not exist\n")
        return#exit function

    #get Birthday
    while True:
        birthday_str = input("Please enter your birth date (DD/MM/YYYY):\n")
        try:
            birthday = datetime.strptime(birthday_str, "%d/%m/%Y")
            days_delta = datetime.today() - birthday#the gap between today & birthday
            age = (days_delta).days//365  #"//"division, but return integer
            if age < 18:
                print("You are too young to rent a car, sorry!\n")
                return
            elif age > 75:
                print("You are too old to rent a car, sorry!\n")
                return
            else:
                print("Age ok")
                break
        except ValueError:
            print("There is not such a date. Try again!")
    #check if user is in "Customer.txt"
    user_exist = False
    file = open("customers.txt","r")
    lines = file.read().splitlines()
    file.close()
    
    for line in lines:
        customer_info = line.split(",")
        if customer_info[0] == birthday_str:
            user_exist = True
            first_name = customer_info[1]
            last_name = customer_info[2]
            print(f"Hello {first_name} ")
            print(f"You rented the car {plate_number}\n")
            break

    #get Name
    if user_exist == False:
        while True:
            print("Names contain only letters and start with capital letters")
            first_name = input("Please enter your first name\n")
            last_name = input("Please enter your last name\n")
            #check if 1)input isn't blank 2)only letter 3)first is Capital 4)others are not Capital
            if (first_name != "" and first_name.isalpha() and last_name.isalpha() and
                first_name[0].isupper() and first_name[1:].islower() and
                last_name[0].isupper() and last_name[1:].islower()):
                break
        #get Email after name is done
        while True:
            email = input("Give your email:\n")
            #check if 1)contains @  2)after @, there is"."
            if "@" in email and "." in email.split("@")[-1]:
                break
            else:
                print("Give a valid email address")
        

        #store info in "customer.txt"
        file=open("customers.txt","a")
        file.write(f"{birthday_str},{first_name},{last_name},{email}\n")
        print(f"Hello {first_name} ")
        print(f"You rented the car {plate_number}\n")
        file.close()
    #store rent info in "rentedVehicles.txt"
    rent_time = datetime.now().strftime("%d/%m/%Y %H:%M")
    file = open("rentedVehicles.txt","a")
    file.write(f"{plate_number},{birthday_str},{rent_time}\n")
    file.close()

def return_car(cars_file,rented_file):
    plate_number=input("Give the register number of the car you want to return:\n")

    available_cars, rented_cars = get_list(cars_file, rented_file)

    #check if the car is in "vehicles.txt", and read price
    car_exist = False
    price_day = 0
    file = open("vehicles.txt","r")
    vehicles = file.read().splitlines()
    file.close()
    for vehicle_line in vehicles:
        vehicle_info = vehicle_line.split(",")
        if vehicle_info[0] == plate_number:
            car_exist = True
            price_day = float(vehicle_info[2])
            break
    #if doesn't exist, back to menu
    if car_exist == False:
        print("Car does not exist\n")
        return

    #check if the car is rented
    car_rented = False
    rented_line = 0
    file=open("rentedVehicles.txt","r")
    rented_lines = file.read().splitlines()
    file.close()

    #find this in "rentedVehicles.txt" then remove it
    for line in rented_lines:
        if line.split(",")[0] == plate_number:
            car_rented = True
            rented_line = line#store this line as rented_line
            rented_lines.remove(line)
            break
    #if the inputted car isn't rented, back to menu
    if car_rented == False:
        print("Car is not rented\n")
        return

    #get the start time of rent
    rented_info = rented_line.split(",")
    start_time = datetime.strptime(rented_info[2], "%d/%m/%Y %H:%M")

    #calculate rent days and cost
    return_time = datetime.now()
    rental_days = (return_time - start_time).days
    real_days = rental_days + 1#if day is <1, round it to 1
    cost = real_days * price_day
    return_time_str = return_time.strftime("%d/%m/%Y %H:%M")

    #write rent info in "transActions
    file = open("transActions.txt","a")
    file.write(f"{plate_number},{rented_info[1]},{rented_info[2]},{return_time_str},{real_days},{cost:.2f}\n")
    file.close()

    #update info in "rentedVehicles.txt"，aka remove this car
    file = open("rentedVehicles.txt","w")
    for line in rented_lines:
        file.write(f"{line}\n")
    file.close()

    #print rent time and cost
    print(f"The rent lasted {real_days} days and the cost is {cost:.2f} euros\n")

def count_money():
    file = open("transActions.txt","r")
    lines = file.read().splitlines()

    #read the cost for each line and store them in total_money
    total_money = 0
    for line in lines:
        each_money = float(line.split(",")[-1])
        total_money += each_money

    print(f"The total amount of money is {total_money:.2f} euros\n")
    file.close()

def main():
    while True:
        try:
            choice=menu()
            if choice==1:
                 print("The following cars are available:")
                 list_available("vehicles.txt", "rentedVehicles.txt")
            elif choice==2:
                 rent_a_car("vehicles.txt", "rentedVehicles.txt")
            elif choice==3:
                  return_car("vehicles.txt", "rentedVehicles.txt")
            elif choice==4:
                count_money()
            elif choice==0:
                print("Thank you for using my program!Bye!")
                break
            else:
                print("Invalid choice. Try again\n")
        except:
            print("Invalid choice. Try again\n")



main()
