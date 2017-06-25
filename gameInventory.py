# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
from collections import Counter
# Displays the inventory.
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(inventory):
    print('Inventory:')
    for key, val in inventory.items():
        print(str(val) + ' ' + (str(key)))
     print('Total number of items:' + str(sum(inv.values())))
inventory = inv

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    loot_dict = {x: added_items.count(x) for x in added_items}
    invent = dict(Counter(inventory) + Counter(loot_dict))
    return invent

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    order = str(input('Write  \'count,desc \' to see descending order and  \'count,asc \' to see ascending order, otherwise press Enter: '))
    print('Inventory:  ')
    print('{:>2}\t{:>12}'.format('count', 'item name'))
    print('- - - - - - - - - - -')
    if order == 'count,desc':
        inventory_desc = sorted(inventory, key=inventory.get, reverse=True)
        for r in inventory_desc:
            print('{:>2}\t{:>12}'.format(inventory[r], r))
    elif order == 'count,asc':
        inventory_asc = sorted(inventory, key=inventory.get)
        for r in inventory_asc:
            print('{:>2}\t{:>12}'.format(inventory[r], r))
    else:
        for key, val in inventory.items():
            print('{:>2}\t{:>12}'.format(val, key))
    print('- - - - - - - - - - -')
    print('Total number of items:' + str(sum(inventory.values())))



# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename):
    import csv
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            my_list = list(row)
        file_dict = {x: my_list.count(x) for x in my_list}
        invent = dict(Counter(inventory) + Counter(file_dict))
        print_table(invent, order)



# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename):
     key_list = []
    for k,v in inventory.items():
        for i in range(0, v):
            key_list.append(k)
    print(key_list)
    with open(filename, "w") as f:
        for item in key_list:
           f.write(item + ', ')
