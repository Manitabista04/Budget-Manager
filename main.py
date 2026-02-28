#def budget():
    #categories: food, rent, utilities, transportation, shopping, entertainment, savings
import json

# New data to add
new_data = {"name": "khebde", "age": 21}


# Step 1: Read existing data
with open("data.json", "r") as file:
    data = json.load(file)

# Step 2: Add new data
data.append(new_data)

# Step 3: Write back to file
with open("data.json", "w") as file:
    json.dump(data, file,indent=4)

print("data append success")

m