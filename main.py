# #def budget():
#     #categories: food, rent, utilities, transportation, shopping, entertainment, savings

# print("data append success")
import json
def addBudget():
    Categories= {}
    Categories["Month"]=input("Month :")
    Categories["Rent"]=input("Rent :")
    Categories["Food"]=input("Food :")
    Categories["Utilities"]=input("Utilities :")
    Categories["Shopping"]=input("Shopping :")
    Categories["Entertainment"]=input("Entertainment: ")
    Categories["Savings"]=input("Savings: ")

    with open("budget.json", "r") as file:
        data = json.load(file)

    # Step 2: Add new data
    data.append(Categories)

    # Step 3: Write back to fileeeeeeeeeeee
    with open("budget.json", "w") as file:
        json.dump(data, file,indent=4)

def addExpenses():    
    expenses={}
    Categories = input("Enter which expenses is it: ")
    valid=["food","rent","savings","utilities","entertainment"]
    if Categories not in valid:
        print("invalid category")
        return 
    name=input("Enter name: ")
    price=input("Enter price: ")
    date=input("Enter date: ")
    expenses = {"name": name , "price" : price ,"date": date}

    with open("expenses.json", "r") as file:
        data = json.load(file)


    if Categories=="food" : 
        data[0]["food"].append(expenses)
    elif Categories=="rent" : 
        data[0]["rent"].append(expenses)
    elif Categories=="savings" : 
        data[0]["savings"].append(expenses)
    elif Categories=="entertainment": 
        data[0]["entertainment"].append(expenses)
    elif Categories=="utilities" : 
        data[0]["utilities"].append(expenses)
    
    with open("expenses.json", "w") as file:
        json.dump(data, file,indent=4)

    print("do you want to add more expenses? (y/n)")
    answer=input()
    if answer=="y":
        addExpenses()
      
def getExpenses():
    with open("expenses.json","r") as file :
        data=json.load(file)
        return data
def getBudget():
    with open("budget.json","r") as file:
        data =json.load(file)
        return data
