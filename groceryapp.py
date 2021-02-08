

stores = []

# Focus on adding stores first.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []

print("Type 1 to add a store: ")
print("Type 2 to add an item to a store: ")
print("Type q to quit: ")

While True:
    choice = input("Enter choice: ")
    if choice == "1":
        store_name = input("Please enter store name: ")
        store_address = input("Please enter store address: ")
        store = Store(store_name, store_address)
        stores.append(store)

    elif choice == "2":
        # display all stores
        
# class Grocery_Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

# store = Store(input("Please enter Store name: "), input("Please enter the address: "))
# stores.append(store)

# print(store.name)
# print(store.address)
# print(stores)

