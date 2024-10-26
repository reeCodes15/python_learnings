# Shape classes
class Shape:
    def area(self):
        return "Area"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Using polymorphism with inheritance
circle = Circle(5)
square = Square(4)

print(circle.area())
print(square.area())

# Person class with nested Dob class
class Person:
    class Dob:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year

        def showdate(self):
            print(f"{self.day}/{self.month}/{self.year}")

    def __init__(self, id, name, addr, day, month, year):
        self.id = id
        self.name = name
        self.addr = addr
        self.db = self.Dob(day, month, year)

    def showinfo(self):
        print('Id:', self.id)
        print('Name:', self.name)
        print('Address:', self.addr)
        self.db.showdate()


p1 = Person(1, 'Reena', 'Ulhasnagar', 15, 10, 1999)
p1.showinfo()

