"""
import datetime as dt
today = dt.datetime.today().strftime('%Y:%m:%d')
print ("Today's date is: ", today)
curr_time = dt.datetime.now().strftime('%H:%M:%S')
print ("Current time: ", curr_time)
remaining = 145-27
print (" You have ", remaining, ("miles remaining on this road"))


first = "maryland"
a =first[2:]
b = first[:2]

second = "England"
c = second[:2]
d = second[2:]
str1 = (b + d)
str2 = (c+ a)
print ("After swapping, we have ", str1, ",",str2 )


first = "maryland"
a =first[2:]
b = first[:2]
print ("a", a)
print ("b", b)

second = "England"
c = second[:2]
d = second[2:]
print ("c", c)
print ("d", d)

str1 = (b + d)
str2 = (c+ a)
print ("After swapping, we have ", str1, ",",str2)


state = 'maryland'

for letter in state :
    print (letter)

state = 'maryland'

for letter in state :
    print (letter)
    MyString = 'maryland'
pst = MyString[4]
print(pst)
MyString = 'maryland'
pst = MyString[4]
print(pst)
"""

"""
Myfruit = 'apple'
print (len(Myfruit))


str = "Python is an interesting Language"

print(len(str))

"""

"""
a = "hello"

if "h" in a:
    print("yeah")
if "m" not in a:
    print("hell no")

"""

"""
fruit = "pineapple"
index = 0
while index < len(fruit) :
   letter = fruit[index]
   print(index, letter)
   # index = index + 1

"""

"""
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
       count = count + 1
print (count)

"""

"""
word = 'today is a great day'
count = 0
for letter in word :
    if letter == 'o' :
       count = count + 1
print (count)

"""

"""
for letter in "banana":
    print(letter)


s = 'Monty Python'
print (s[6:7])


s = 'Nine's Python'
print (s[2:9])

"""

"""
s = 'Nine’s Python'
 print (s[:2])
fruit = 'banana’
print ( 'n' in fruit)
fruit = 'banana’
print ( 'n' in fruit)

"""
word = input("please enter your word: ")
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print ('Same word.')


