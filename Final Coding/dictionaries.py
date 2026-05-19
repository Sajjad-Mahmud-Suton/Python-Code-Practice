customer = {
    "name" : "Sajjad Mahmud",
    "age" : 23
}

print(customer["name"])
print(customer.get("birthdate"))
print(customer.get("birthdate", "Dec 1 2003"))
customer["name"] = "Sajjad"
print(customer["name"])