def my_func(param1="default"):
    """
    This is the docstring
    """

    print("my first python function! {}".format(param1))

my_func()

def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Integer only"

result = addNum("2","5")
print(result)

# Lambda Expression

# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)


evens_lambda = filter(lambda num:num%2 == 0, mylist) # lambda is anonymous function
print(list(evens)) # [2, 4, 6, 8]
print(list(evens_lambda)) # [2, 4, 6, 8]

