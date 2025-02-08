from urllib.request import urlopen
import json

print("Welcome to Rick & Morty API")

menu = """You have the following options:
0) Exit
1) Get all dead characters
2) Get characters by their name and living status
Enter your selection:\n"""

def fetch_data(url,max_page): #抓取url中的数据
    all_results = []#存储所有结果
    current_page = 1

    while url is not None and current_page <= max_page:
        print(f"Getting page {current_page} url: {url}")
        try:
            with urlopen(url) as response:
                data = json.load(response)
                #把本页中每个角色加入all
            for character in data["results"]:
                all_results.append(character)
                #获取下一页链接
            url = data["info"]["next"]
            current_page += 1
        except Exception as e:
            print("Error fetching data:",e)
            break

    return all_results

def main():
    while True:
        choice = int(input(menu))
        if choice == 0:
            print("Bye")
            break
        elif choice == 1:
            max_page = int(input("Enter limit of pages: "))
            url = "https://rickandmortyapi.com/api/character/?status=dead"
            dead_data = fetch_data(url,max_page)
            number = 0
            for character in dead_data:
                print(f"Id:{character['id']} - name:{character['name']} - type:{character['type']} - species:{character['species']} - status:{character['status']}")
                number += 1
            print(f"Total number of characters: {number}")
        elif choice == 2:
            name = input("Enter character to search for: ")
            status = input("Enter living status (alive, dead, unknown): ")
            max_page = int(input("Enter limit of pages: "))
            #根据输入修改url
            url = f"https://rickandmortyapi.com/api/character?name={name}&status={status}"
            filtered_data = fetch_data(url,max_page) #里面是按name status筛选过的数据
            number = 0
            for character in filtered_data:
                print(f"ID:{character['id']} - name:{character['name']} - type:{character['type']} - species:{character['species']} - origin:{character['origin']['name']} - status:{character['status']}")
                number += 1
            print(f"Total number of {status} {name}'s found: {number}")

main()


