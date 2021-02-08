
class Customer:
    def __init__(self, name):
        self.name = name
        self.addresses = [] # array to represent addresses

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

customer = Customer("John Doe")
print(customer.addresses)
address = Address("1200 Richmond Ave", "Houston", "TX", "77989")
#how to add address to a customer
customer.addresses.append(address)

#display customer and address
print(customer.addresses)
for address in customer.addresses:
    print(address.street)
    print(address.state)


# customer.street = "1200 Richmond Ave"
# customer.city = "Houston"
# customer.state = "TX"
# customer.zip_code = "77890"

#Post
#Comment
#A single Post can have many comments

Walmart
- Paper
- Shirts
- Shoes

Kroger
- Meat
- Chicken

Whole Foods 
- Fruit
- vegetable
