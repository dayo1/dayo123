"""
import datetime

print ("Current date and time: " , datetime.datetime.now() )
print ("Current date and time: " , datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

"""

"""
import datetime

print ("Current date and time: " , datetime.datetime.now() )
print ("Current date and time: " , datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
print ("Current year: ", datetime.date.today().strftime("%Y") )
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Week number of the year: ", datetime.date.today().strftime("%W"))
print ("Weekday of the week: ", datetime.date.today().strftime("%w") )
print ("Day of year: ", datetime.date.today().strftime("%j"))
print ("Day of the month : ", datetime.date.today().strftime("%d"))
print ("Day of week: ", datetime.date.today().strftime("%A"))

"""

"""
import datetime as dt
from datetime import date, timedelta

Now = dt.datetime.now()
print("Welcome to 9-Solutions Shopping Center")
print("Current time: ")
print(Now.strftime(" %H:%M"))
print("Closing time for today is 11:00pm")
close = (timedelta(hours=23) - (Now - Now.replace(hour=0, minute=0)))
print("You have", close, "hours for your shopping today")

"""

"""
import random
a = random.randint(1,10)
d = random.randrange(2,43,3)
ch = random.choice("Python is an interesting Language".split())
print ("random integer pick 1 to 10:", a)
print ("random pick from 2 to 43 range :", d)
print ("random choice:", ch)

"""

"""
str1 = "Hello, Welcome  "
str2 = ' to today’s class'
msg = str1 + str2
print(msg)

"""
"""
str1 = "Hello, Welcome  "
str2 = ' to today’s class'

msg = str1 + str2
print(msg)
#str3 = '456'
#str4 = str3 + 1
#print(str4)
str3 = '456'
str4 = int(str3) + 1
print(str4)

"""

"""

MyVar1= 'Hello world'
print(type(MyVar1))
print( dir(MyVar1))
"""

"""
MyVar1= 'Hello world'
print(type(MyVar1))
for item in dir( dir(MyVar1)):
    print (item)

"""

"""
MyStr = "Happy Moments"

print (MyStr[:2])
print (MyStr[3:5])
print (MyStr[2:])
print (MyStr[1:6])

"""


"""
speed = "500 m/s"
x = speed[:]
print(x)


speed = "500 m/s"
x = speed[:2]
print(x)


speed = "500 m/s"
x = speed[4:]
print(x)


fruit = 'apple'

for letter in fruit :
    print (letter)

"""

"""
MyStr = 'Maryland'
print (MyStr[7])
MyStr = 'Maryland'
print (MyStr[4])



s = 'Nine’s Python'
print (s[:2])


a = 'Hello'
b = a + 'Students'
print (b)


a = 'Hello'
b = a + 'Students'
c=a +' '+'Students'
print (b)
print (c)

"""
"""
import datetime as dt
from datetime import date, timedelta
Now = dt.datetime.now()
print("Welcome to 9-Solutions Shopping Center")
print("Current time: ")
print(Now.strftime(" %H:%M"))
print("Current date: ")
print(dt.datetime.today())
print("Closing time for today is 11:00pm")
close = (timedelta(hours=23) - (Now - Now.replace(hour=0, minute=0)))
print("You have", close, "hours for your shopping today")

"""

"""
import datetime
print("Welcome")
now = datetime.datetime.now()
print("Today's Date and Current time: ")
print(now.strftime("%Y-%m-%d %H:%M"))
print("You have 118 miles to your destination")

"""
"""
import datetime as dt
from datetime import date, timedelta
Now = dt.datetime.now()
print("Welcome to 9-Solutions Shopping Center")
print("Current time: ")
print(Now.strftime(" %H:%M"))
print("Current date: ")
print(dt.datetime.today())
print("Closing time for today is 11:00pm")
close = (timedelta(hours=23) - (Now - Now.replace(hour=0, minute=0)))
print("You have", close, "hours for your shopping today")

"""

MyStr = 'Maryland'
print (MyStr[7])
MyStr = 'Maryland'
print (MyStr[4])



s = 'Nine’s Python'
print (s[:2])


a = 'Hello'
b = a + 'Students'
print (b)


a = 'Hello'
b = a + 'Students'
c=a +' '+'Students'
print (b)
print (c)

string1 = "Maryland"
string2 - "England"

