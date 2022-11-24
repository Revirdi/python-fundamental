print((1 > 2) and ( 2 < 3)) # False
print((1 > 2) or ( 2 < 3)) # True

if 1<2:
    print('yes')

if 1<2:
    print('First BLock')
    if 2 < 3:
        print('Second Block')

if 3 < 2:
    print('Hello')
elif 3 == 3:
    print('elif run')
else:
    print('last')

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

d = {"sam": 1, "Frank": 2, "Dan": 3}
for item in d:
    print(item) # sam Frank Dan (un-ordered, bisa berubah2 penempatannya)

for item in d:
    print(d[item]) # 1 2 3 (un-ordered, bisa berubah2 penempatannya)

mypairs = [(1,2), (3,4), (5,6)]

for item in mypairs:
    print(item) # (1,2) (3,4) (5,6)

for tup1, tup2 in mypairs:
    print(tup2)
    print(tup1)
# 2 1 4 3 6 5

i = 1
while i<5:
    print("i is: {}".format(i))
    i = i+1

print(list(range(0, 5))) # [0, 1, 2, 3, 4]
print(list(range(1, 5))) # [1, 2, 3, 4]
print(list(range(0, 20, 2))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

for item in range(10):
    print(item) # 0,1,2,3,4,5,6,7,8,9

x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)

print(out) # [1, 4, 9, 16]

out2 = [num**2 for num in x]
print(out2) # [1, 4, 9, 16]
print(list(map(str,out2)))