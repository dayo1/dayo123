"""
level = int(input("In what class are you now? "))
print ("Your level is", level)
print ("You have", 5 - level, "years until graduation")
"""
"""
name = input("what is your name")
adv = input("enter a qualifier")
print ("Welcome to today's class", adv, name)


name = input("Enter your name please:")
adj = input("Enter a qualifier :")
print("Hello", adj,“", name,"! Welcome to today’s Python Class" )

"""

"""
x = int( input ("enter the first number: "))
y = int(input ("enter the second number: "))
a = x+y
print (a)

z = int( input ("enter the third number:"))
b = a*z
print (b)

c = b**2
d = pow(b,2)
print (c)
print (d)
"""

"""
import random

ourrand = random.randint(0, 99)

your_num = int(input("Enter your favorite number :"))

if ourrand == your_num:
    print (your_num, "is equal to", ourrand )

else:
    print (your_num, "is not equal to", ourrand )

"""

"""
name = input("My name is: ")
adj = input("qualifier: ")
print(adj, name)

name = input("Enter your name please:")
adj = input("Enter a qualifier :")
print("Hello", adj,"", name, "! Welcome to today’s Python Class" )

"""

"""
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
a = x+y
print(x, y)
print(a)

z = int(input("enter the third number:"))
b = a*z
print(b)

c = b**2
d = pow(b,2)
print(c)
print(d)

"""

"""
from math import pi

r = int(input(" Abeg, enter the radius of the circle: "))
area = pi * r **2
print("The area of the cirle =", area)

"""

"""
v = int(input("Abeg, enter a number: "))
t = v*5
z = t**6
print(z)

"""

"""
name = input (" Please enter your name: ")
loc = int(input (" Please enter your location: "))
dest = 125 - loc
print ("Hello", name, ', You have ', dest, "miles until your destination")

"""

"""
import math
r = int(input("Please enter the radius of the cylinder: "))
h = int(input("Please enter the height of the cylinder: - "))
b_area = 2* math.pi *r **2
s_area = h * 2* math.pi* r

Surface_area = b_area + s_area
print ("Base Area:", b_area)
print("Side Area:", s_area)
print("Total Surface Area:", Surface_area)
print("Total Surface Area:", round( Surface_area,2))

"""

"""
x= True
y= False

print ("X and Y:", x and y)
print ('X or Y:', x or y)
print ("not of x:", not x)
x= True
y= False

print ("X and Y:", x and y)
print ('X or Y:', x or y)
print ("not of x:", not x)
"""

"""
a =[1,2,3,4,5,6]
print(4 in a)
print(4 not in a)
"""

"""
import random

ourrand = random.randint(0, 99)
count =0
while (True):
    your_num = int(input("Enter your favorite number :"))
    count += 1
    if your_num < ourrand:
        print("You number",your_num, "is lower than our system's number")
    elif your_num > ourrand:
        print("You number", your_num, "is greater than our system's number")
    else:
        print(" Hurray!!, You got it in", count, "trials")
        break
"""

"""
import random
d = random.randrange(2,43,3)
ch = random.choice("Every_Step")
print (str(d) + ch)

"""

"""

import random
import string
import secrets

s = string.ascii_lowercase + string.digits + string.ascii_uppercase + "@#$%&_-*"

print(''.join(secrets.choice(s) for _ in range(random.randint(8, 12))))
print("Please change your password after logging in")

"""


import datetime

print ("Current date and time: " , datetime.datetime.now() )
print ("Current date and time: " , datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
print ("Current time: " , datetime.datetime.now().strftime("%H-%M"))

