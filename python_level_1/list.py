# mylist = [1,2,3]
# mylist = ['string stuff', 1,2,3,42, True, [1,2,3]]
# print(len(mylist)) # length

# mylist = ['a', 'b', 'c']
# print(mylist[1])

# mylist = ['a','b','c']
# print('before:', mylist) # before: ['a', 'b', 'c']
# mylist[0] = "NEW ITEM"
# mylist[1] = False
# print("after:", mylist) # after: ['NEW ITEM', False, 'c']


# mylist = ['a','b','c']
# mylist.append("NEW ITEM") 
# print(mylist) # ['a', 'b', 'c', 'NEW ITEM']


# mylist = ['a','b','c']
# mylist.append([1,2,3]) # ['a', 'b', 'c', [1, 2, 3]]
# mylist.extend([1,2,3]) # ['a', 'b', 'c', 1, 2, 3]
# print(mylist)

# mylist = ['a','b','c']
# item = mylist.pop() # delete last index
# item = mylist.pop(0) # delete index ke 0
# print(mylist) # ['a', 'b']
# print(item) # c

# mylist = ['a','b','c']
# mylist.reverse() 
# print(mylist) # ['c', 'b', 'a']

# mylist = [1,2,4,23,19,40]
# mylist.sort()
# print(mylist) # [1, 2, 4, 19, 23, 40]

# mylist =[1,2,['x', 'y', 'z']]
# print(mylist[2][1]) # y

# list comprehension
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# first_col = [row[0] for row in matrix]
# print(first_col) # [1, 4, 7]