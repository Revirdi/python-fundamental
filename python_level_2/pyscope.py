name = "This is a global name"

def greet():
    name = "sammy"

    def hello():
        print("hello "+ name)
    
    hello()

greet()
print(name)