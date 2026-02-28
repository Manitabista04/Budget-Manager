# #def budget():
#     #categories: food, rent, utilities, transportation, shopping, entertainment, savings
# import json

# # New data to add
# new_data = {"name": "khebde", "age": 21}


# # Step 1: Read existing data
# with open("data.json", "r") as file:
#     data = json.load(file)

# # Step 2: Add new data
# data.append(new_data)

# # Step 3: Write back to file
# with open("data.json", "w") as file:
#     json.dump(data, file,indent=4)

# print("data append success")

def budget():
    Categories= {
        "Month" : "January",
        "Rent" : 250,
        "Food" : 100,
        "Utilities" : 40,
        "Entertainment" : 10,
        "Shopping" : 5,
        "Savings" : 0,
    }
    Categories["Month"]=input("Month :")
    rent=input("Rent :")
    Food=input("Food :")
    utilities=input("Utilities :")
    Shopping=input("Shopping :")


    print(Categories["Month"])
    print(Categories)
    print("done!")
  

budget()