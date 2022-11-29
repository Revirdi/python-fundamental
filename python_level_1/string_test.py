mystring = 'abc defg'

# indexing
print(mystring[0]) # a
print(mystring[-1]) # g

# Slicing
print(mystring[2:]) # cdefg
print(mystring[4:]) # efg
print(mystring[:3]) # abc index ke-3 tidak include
print(mystring[2:5]) # cde
print(mystring[::2]) # aceg lompat 1 huruf

# basic methods
mystring.upper() # jadi uppercase semua
mystring.lower() # jadi lowercase semua
mystring.capitalize() # Huruf pertama jadi uppercase
print(mystring.split()) # ['abcdefg']


# Formatting
test = "Insert another string here: {}".format("insert me") # Insert another string here: insert me
test2 = "Insert another string here: {} {}".format("insert me", "bro") # Insert another string here: insert me bro
test3 = "Item One : {x} Item Two : {y}".format(x = "cat", y = "dog") # Item One : cat Item Two : dog





