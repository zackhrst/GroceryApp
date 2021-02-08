stores = []

# Focus on adding stores first.

class Shopping_List:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Grocery_Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

store = Store(input("Please enter Store name: "), input("Please enter the address: "))
stores.append(store)

print(store.name)
print(store.address)
print(stores)

