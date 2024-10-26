# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

class Car:
    def __init__(self, model, brand):
        self.model = model 
        self.brand = brand
    
    def start_engine(self):
        print("Engine started for ", self.model)
        


balenoCar = Car("Baleno", "Guddi")

cretaCar = Car("Creta", "Laila")

balenoCar.start_engine()
cretaCar.start_engine()




# Base class Person
class Person:
    cn = "Snickerdoodle Cafe"
    np = 0  

    def __init__(self, id, name, address):
        self.id = id  
        self.name = name 
        self.address = address  
        Person.np += 1 
        
    def name(self):
        print("Person is having name -", self.name)
        
class Teacher(Person):
    def __init__(self, id, name, address, subject, experience):
        super().__init__(id, name, address)
        self.subject = subject  
        self.experience = experience 
        
    def display_info(self):
        print(f"Teacher {self.name} teaches {self.subject} and has {self.experience} years of experience.")
        super().name()
    

# Creating instances of Person
p1 = Person(1, "Ree-bitch", "Ulhasnagar")
p2 = Person(2, "Feku", "Kalyan")

print("Persons:")
print(p1.name)
print(p2.name)

t1 = Teacher(3, "Mr. Sharma", "Mumbai", "Mathematics", 10)

print("\nTeacher:")
t1.display_info()
print(f"\nTotal number of persons: {Person.np}")
