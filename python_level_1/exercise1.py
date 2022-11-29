s = 'django'
print(s[0]) # d
print(s[-1]) # o
print(s[:4]) # djan
print(s[1:4]) # jan
print(s[4:]) # go
print(s[::-1]) # ognajd (reverse string)
print(list(s)) # ['d', 'j', 'a', 'n', 'g', 'o'] (kaya split('') di javascript)
print([c for c in s]) # ['d', 'j', 'a', 'n', 'g', 'o'] for loop

l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l) # [3, 7, [1, 4, 'goodbye']]

d1 = {'simple_key': 'hello'}

d2 = {'k1':{'k2': 'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key']) # hello
print(d2['k1']['k2']) # hello
print(d3['k1'][0]['nest_key'][1][0]) # hello

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]
print(list(set(mylist))) # [1, 2, 3]

age = 4
name = 'Sammy'

print(f"Hello my dog's name is {name} and he is {age} years old") # Hello my dog's name is Sammy and he is 4 years old 