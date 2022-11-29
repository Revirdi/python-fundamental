# Boolean
True
False

# Tuples
t = (1,2,3)
print(t[0]) # 1

t = ('a', True, 123) # ('a', True, 123)
print(t)
# t[0] = 'NEW' # TypeError: 'tuple' object does not support item assignment

# Sets (un-ordered)

x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
print(x) # {0.1, 1, 2, 4} (acak, tidak berurutan, ) 
x.add(4)
print(x) # {0.1, 1, 2, 4} (no repead element, value 4 tidak akan masuk 2x)

