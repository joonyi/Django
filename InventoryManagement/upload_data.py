import json

def update_inventory():
    with open('data.json', 'r') as inventory_data:
        for line in inventory_data.readlines():
            inventory = json.loads(line)
            # for i in inventory:
            print(inventory['name'])
            print(inventory['description'])
            print(inventory['note'])
    return


update_inventory()
