class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):
        print(self.name, "- Price:", self.price, ", Stock:", self.stock)

p1 = Product("Lipstick", 150, 20)
p2 = Product("Mascara", 450, 5)
p3 = Product("Foundation", 300, 0)

p1.show_info()
p2.show_info()
p3.show_info()
