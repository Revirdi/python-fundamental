# Inheritance

class Animal():
    
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")

mya = Animal() # Animal Created
mya.whoAmI() # Animal
mya.eat() # Eating

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("DOG CREATED")
    
    def bark(self):
        print("Woof")
    
    def eat(self): # Overide method "eat" from class Animal
        print("Dog Eating")

myd = Dog() # DOG CREATED
myd.whoAmI() # Animal
myd.eat() # Eating
myd.bark() # Woof


# Special Methods
print("*************************************")


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Title : {self.title}, Author : {self.author}, Total Pages: {self.pages}"
    
    def __len__(self):
        return self.pages

    def __del__(self):
        return print("Book is destroyed!")

b = Book("Spiderman", "Revirdi", 200)

print(b) # Title : Spiderman, Author : Revirdi, Total Pages: 200
print(len(b)) # 200
del b # Book is destroyed!