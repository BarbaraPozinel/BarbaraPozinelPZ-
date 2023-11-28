import json

with open(r"C:\Users\Admin\Downloads\users.json", "r") as users_file:
    data = json.load(users_file)

search = input("Enter last name: ")

for person in data:
    full_name = person["name"].split()
    first = full_name[0]
    last = full_name[1]

    if last.lower() == search.lower():
        print("Name:", person["name"])
        print("Email:", person["email"])
        print("Company name:", person["company"]["name"])
        break

    else:
        print("Last name:", last)
        print("First name:", first)
        print("Latitude of the city:", person["address"]["geo"]["lat"])
        print(person["company"]["catchPhrase"] + "\n")

