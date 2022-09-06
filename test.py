class Students:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(self.name, self.roll)

    class Laptop:
        def __init__(self):
            self.ram = 12
            self.brand =  'dell'
        def show(self):
            print(self.ram, self.brand)

s1 = Students('sano', 12)
s1.show()
laptop = Students.Laptop()
laptop.show()
