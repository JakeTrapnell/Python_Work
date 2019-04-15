customer = {
    "name": "Jake",
    "age": 26,
    "is_verified": True
}
customer["birth_date"] = "17/10/1992"
print(customer["name"])
print(customer)

phone = input("phone: ")
numbers_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
}
output = ""
for ch in phone:
    output += numbers_mapping.get(ch, "!") + " "
print(output)