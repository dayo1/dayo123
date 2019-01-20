"""

counts = {}
countries = ['Albania', 'Algeria', 'Angola', 'Aruba', 'Argentina', 'Andorra', 'Angola', 'Armenia', 'Andorra', 'Aruba', 'Angola']
for name in countries :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
        print(counts)

"""

"""
counts = {}
names = ['rose', 'john', 'peter', 'john', 'robin', 'farry', 'robin']
for name in names:
    if name not in counts:
        counts[name] = counts.get(name, 1) + 1
    else:
        counts[name] = counts[name] + 1
        print(counts)
"""

"""
count = {}
print("Enter a line of text:")
line = input('')
words = line.split()

print("Counting...")

"""

"""
for word in words:
    counts[word] = counts.get(word,0) + 1
    print(counts)
    
 """

"""
x = {'a':1, 'b':2, 'c':3, 'd':4} #dictionary
if 'a' in x:
    del x['a']
    print(x)
"""

"""
my_dict= {'Ab':100,'BC':-94,'CD':247, 'DE':710}
print(sum(my_dict.values()))

max_value=max(my_dict.items(),key=lambda k:k[1])
print(max_value)

"""

"""
def simpleme(str):
    "This prints a passed string into this function"
    print(str)
    return;
# Now you can call simpleme function
simpleme(str = 'This is me')

"""

"""
def multiply(nums):
    result = 1
    for x in nums:
        result *= x
        return result
    my_numbs = [3,4,6,10,2,1]
    print(multiply(my_numbs))

"""

"""

def multiply(nums):
    result = 1
    for x in nums:
        result *= x
    return result
my_numbs = [3, 4, 6, 10, 2, 1]
print(multiply(my_numbs))

"""

"""
from math import factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int (input("Input a number to compute the factorial:"))
print(factorial(n))

"""

"""
def reverse(x):
    y =x.split()
    y.reverse()
    return "".join(y)
My_str = "Python is an interesting lanaguage"
print (reverse(My_str))

"""

"""

def check_num(my_list, n):
    if n in my_list:
        print(n, "this is in the list")
        return True
    else:
        print(n, "This is not in this list! ")
        return False
print(check_num(range(2,19), 20))

"""

"""
def computepay():
    # This function returns staff payment
    hrs: int = int (input ("Please enter hours: "))
    rate = int (input("Please enter rate: "))
    if hrs <= 40:
        pay = hrs * rate
    else:
        pay = (40 * rate) + ((hrs -40) * (rate *1.5))
    return print(pay)
computepay()

"""

def computepay():
    # This function returns staff payment
    hrs: int = int (input ("Please enter hours: "))
    rate = int (input("Please enter rate: "))
    if hrs <= 40:
        pay = hrs * rate
    else:

        pay1 = (40 * rate)
        print("normal pay is :", pay1)
        pay2 = ((hrs -40) * (rate *1.5))
        print("overtime pay is :", pay2)
    return (pay1 + pay2)
print(computepay())