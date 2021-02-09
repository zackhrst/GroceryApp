

stores = []


# Focus on adding stores first.

class Store:
    def __init__(self, name, address):
        self.store_name = name
        self.store_address = address
        self.items = []

    def add_item(self, item):
        # Check if item is already in store
        # then add item to the items array
        # else ignore it
        pass

    def remove_item(self, item):
        # Check if item is in list
        # then remove item from items array
        # else ignore it
        pass

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# def options():
#     print("Type 1 to add a store. ")
#     print("Type 2 to add an item to a store. ")
#     print("Type 3 to see your Lists. ")
#     print("Type q to quit: ")

# def print_stores():
#     for i in range(0,len(stores)) :
#             store = stores[i]
#             print (f'{store["store_name"]}')

# def print_item_list():
#     print("*** Grocery List***")

# while True:
#     print("Type 1 to add a store. ")
#     print("Type 2 to add an item to a store. ")
#     print("Type 3 to see your Lists. ")
#     print("Type q to quit: ")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         store_name = input("Please enter store name: ")
#         store_address = input("Please enter store address: ")
#         # store = Store(store_name, store_address)
#         store = {"store_name" : store_name , "store_address" : store_address}
#         stores.append(store)

#     elif choice == "2":
#         # display all stores
#         print_stores()
#         store_choice = int(input("Which Store's list are you adding to?: "))
#         name_item = input("What Item are you adding?: ")
#         price = input("How much does the item cost?: ")
#         quantity = input("How many are you buying?: ")
#         new_item = Item(name_item, price, quantity)
#         stores[store_choice - 1].list.append(new_item)

#     elif choice == "3":


#     elif choice == "q":
#         break
        

    # Class Review

print("1. Add Store: ")
print("2. Add Item to Store: ")
print("3. View All")
print("q for Quit")


while True: 
    choice = input("Enter Choice: ")
    if choice == "1":
        store_name = input("Enter Store name: ")
        store_address = input("Enter Store Address: ")
        store = Store(store_name, store_address)
        stores.append(store)
    
    elif choice == "2":
        for index in range(0, len(stores)):
            store = stores[index]
            print(f"{index + 1} {store.store_name} - {store.store_address}")

        store_index = int(input("Choose Store to add items: "))
        store = stores[store_index - 1]
        item_name = input("Enter Item name: ")
        item_price = float(input("Enter Item Price: "))
        item_quantity = int(input("How many are you buying?: "))
        item = Item(item_name, item_price, item_quantity)
        # add item to the store
        #store.add_item(item) # better approach because you can check for duplciates on list and prevent them.
        store.items.append(item)

    elif choice == "3":
        for store in stores:
            print(f"{store.store_name} - {store.store_address}:")
            for item in store.items:
                print(f"{item.name} - ${item.price}")
        # print(stores)


    elif choice == "q":
        break

