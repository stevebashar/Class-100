class Car():
    def __init__(self, brand, color, mileage, model, price):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.model = model
        self.price = price

    def start(self):
        print("The car has started")

    def stop(self):
        print("The car has stopped")

bmw = Car("bmw", "red", 142, "X5" , 20000)
print(bmw.start())
print(bmw.brand)
print(bmw.mileage)
print(bmw.color)