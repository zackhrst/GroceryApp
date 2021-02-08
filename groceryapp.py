

stores = []


# Focus on adding stores first.

class Store:
    def __init__(self, name, address):
        self.store_name = name
        self.store_address = address
        self.list = []

class Item:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

# def options():
#     print("Type 1 to add a store. ")
#     print("Type 2 to add an item to a store. ")
#     print("Type 3 to see your Lists. ")
#     print("Type q to quit: ")

def print_stores():
    for i in range(0,len(stores)) :
            store = stores[i]
            print (f'{store["store_name"]}')

def print_item_list():
    print("*** Grocery List***")

while True:
    print("Type 1 to add a store. ")
    print("Type 2 to add an item to a store. ")
    print("Type 3 to see your Lists. ")
    print("Type q to quit: ")
    choice = input("Enter choice: ")
    if choice == "1":
        store_name = input("Please enter store name: ")
        store_address = input("Please enter store address: ")
        # store = Store(store_name, store_address)
        store = {"store_name" : store_name , "store_address" : store_address}
        stores.append(store)

    elif choice == "2":
        # display all stores
        print_stores()
        store_choice = int(input("Which Store's list are you adding to?: "))
        name_item = input("What Item are you adding?: ")
        price = input("How much does the item cost?: ")
        quantity = input("How many are you buying?: ")
        new_item = Item(name_item, price, quantity)
        stores[store_choice - 1].list.append(new_item)

    elif choice == "3":
        

    elif choice == "q":
        break
        



