# Given a list of integers, return True if the sequence of number 1,2,3
# appears in the list 

def array_check(nums):
    
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

print(array_check([1,1,2,1,2,3,3,2]))

# Given a string, return a new string made of every other character jump 1 time starting
# with the first, so "Hello" yields "Hlo".

def string_bits(mystring):
    result = ""
    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]
    return result
print(string_bits("Hello"))

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences
# example:
# end_other('Hiabc', 'abc') -> True
# end_other('AbC','HiaBc') -> True

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    # return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]
print(end_other('Hiabcd', 'abc'))

def double_char(mystring):
    result = ''
    for char in mystring:
        result += char*2
    return result


# no_teen_sum(1,2,3) -> 6
# no_teen_sum(1,13,2) -> 3
# no_teen_sum(2,1,14) -> 3

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13,14,15,16,17,18,19]:
        return 0
    return n

print(no_teen_sum(1,4,2))

# return the number of even integers in the given array
# Examples:
# count_evens([2,1,2,3,4]) -> 3
# count_evens([1,3,5]) -> 0

def count_evens(nums):
    result = 0
    for i in nums:
        if i % 2 == 0:
            result += 1
    return result

print(count_evens([2,1,2,3,4]))