"""Demostration of __repr__ magic method and appending all instances into an empty list using a python program"""

class Item:

    # Creating an empty list to store all the 5 instances
    all = []    
    
    # Initializing Class Attribute
    pay_rate = 0.8 # Pay rate after discount

    # A constructor for class Item where we have to implement the instance attributes inside the constructor
    def __init__(self, name: str, price: float, quantity = 0):
        
        # Run validations or conditions for the recieved arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0!"
        
        # Assign to self object the Instance attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Creating a magic method repr to represent all the instances in a list named all
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    # Creating a method to calculate the total price of an instance item1 or item2
    def calculate_total_price(self):
        return self.price * self.quantity
         
    # Creating another method to apply Discount to the total price of the object
    def apply_discount(self):
        
        # Using  self.pay_rate enables us to retrieve the class attribute pay_rate 
        self.price = self.price * self.pay_rate

# Creating 5 Instances of class Item 
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)