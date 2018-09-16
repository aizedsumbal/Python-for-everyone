inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'arrow': 12}
def displayInventory(dict):
    print("Inventory")
    total_items = 0
    for k,v in dict.items():
        print(v,k)
        total_items += v

    print("total items ")
displayInventory(inventory)