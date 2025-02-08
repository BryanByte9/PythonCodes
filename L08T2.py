import string, random
LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = string.punctuation
COMB = LETTERS + DIGITS + SPECIAL

while True:
    length = int(input("Enter the length of the password:\n"))
    if length>0:
        random.seed(8292)
        password=""
        i=1
        #Add random number into password one by one
        while i<=length:
            component = random.choice(COMB)
            password = password+component
            i = i+1
        print(f"Generated password: {password}")
        break
    else:
        print("Password length must be a positive integer.")
        

