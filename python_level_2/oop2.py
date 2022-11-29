# class Dog():

#     # Class Object Attribute
#     species = "mammal"
    
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name

# mydog = Dog("Lab","Sammy") # mydog = Dog(breed= "Lab",name= "Sammy")
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)
# otherdog = Dog(breed="Huskie")
# print(otherdog.breed) # Huskie

class Circle():
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def set_radius(self, new_radius):
        self.radius = new_radius

myc = Circle(3) # 3 masuk ke radius di __init__
print(myc.radius) # 3
print(myc.area()) # 28.26

myc.radius = 100
print(myc.area()) # 31400.0

myc.set_radius(50)
print(myc.area()) # 7850.0
