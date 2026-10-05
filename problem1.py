class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def intro(self):
        print("Product: " + self.name + ", Price: " + str(self.price))
p1 = product("Lipstick", 150)
p1.intro()        
        