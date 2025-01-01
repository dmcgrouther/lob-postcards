import json

def load_address_ids(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Call the function with the correct file name as a string
addresses = load_address_ids("data.json")
print(addresses)

for address in addresses:
    print(address)