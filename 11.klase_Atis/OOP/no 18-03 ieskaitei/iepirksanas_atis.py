from abc import ABC, abstractmethod

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        #aprēķina kopējo cenu un parāda to
        return (f"Name: {self.name}, total price: {self.price * self.quantity}$")

products = [
Product("T-shirt", 23, 250),
Product("Hoodie", 36, 250)
]

for x in products:
    print(x.get_total_price())
    
#cart_contents = []
#cart_contents_prices = []
class ShoppingCart():
    def __init__(self):
        self.cart_contents = []
        self.cart_contents_prices = []
    def add_product_to_cart(self, product):
        self.cart_contents.append(product.name)
        self.cart_contents_prices.append(product.price)
        return (f"Item: {product.name} has been added to the cart.")
    def remove_product_from_cart(self, product):
        if product.name not in self.cart_contents:
            return (f"Item is not in the cart!")
        else:
            self.cart_contents.remove(product.name)
            self.cart_contents_prices.remove(product.price)
            return (f"Item has been removed from the cart.")
    def get_total_price(self):
            p = 0
            for x in self.cart_contents_prices:
                p = p + x
            return (f"Total cart price: {p}$")

cart1 = ShoppingCart()



for x in products:
    print(x.get_total_price())

for x in products:
    print(cart1.add_product_to_cart(x))

print(cart1.get_total_price())  

class SystemUser():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    def set_user_info(self, password, email): 
        self.password = password
        self.email = email
        return (f"User info has been updated!")
    def get_user_info(self):
        return (f"Username: {self.username}, Password: {self.password}, E-mail: {self.email}")

#izsauc admina lietotāja izveidi
admin = SystemUser("admin", "password123", "admin@shop.com")
print(admin.get_user_info())
print(admin.set_user_info("password1234", "admin@zebestshop.com"))
print(admin.get_user_info())

#pievieno īpašo klasi
class Customer(SystemUser):
    def __init__(self, username, password, email):
        super().__init__(username, password, email)
        self.customer_id = 0
        self.purchase_history = ""
        self.membership_status = False
    def set_user_info(self, password, email, purchase_history, memberhsip_info):
        self.password = password
        self.email = email
        self.purchase_history = purchase_history
        self.membership_status = memberhsip_info 
        return super().set_user_info(password, email)

