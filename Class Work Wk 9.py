"""

List1= [1, 2, 3, 4, 5, 5,5,6,7,8,9,0]
List2=[88,87,86,84,89,45,89,14]
count1 = 0
count2 = 0
x = int(input("please select a number from the list: "))

for i in List1:
    if x ==i:
        count1= count1 + 1
print(count1)

"""

"""
x = 1.16
y = 2.05
High_performers =[]
Good_performers =[]
Average_performers =[]

while (True):
    name = input( "Enter the Staff name please: ")
    a = int(input("Enter the number of previous promotions: "))
    b = int(input("How many endorsement have you received? : "))
    c = int(input("Enter number of years : "))


    rating = (a * x **3 ) + (b * y*2) + c
    if rating > 19:
        print (" Congratulations!", name, "You belong to first class performers")
        High_performers.append(name)
    elif rating >= 11:
        print(" Congratulations!", name, "You will be promoted, as a middle-class performer")
        Good_performers.append(name)
    else:
        print(" Please work harder next time!")
        Average_performers.append(name)

    resp = input("More staff? Enter 0 to quit:")
    if resp == "0" :
        break
    else:
        continue

print( "High Performers:", High_performers)
print( "Good Performers:", Good_performers)
print( "Average Performers:", Average_performers)

"""

"""
x = 1.16
y = 2.05
High_performers =[]
Good_performers =[]
Average_performers =[]

while (True):
    name = input( "Enter the Staff name please: ")
    a = int(input("Enter the number of previous promotions: "))
    b = int(input("How many endorsement have you received? : "))
    c = int(input("Enter number of years : "))


    rating = (a * x **3 ) + (b * y*2) + c
    if rating > 19:
        print (" Congratulations!", name, "You belong to first class performers")
        High_performers.append(name)
    elif rating >= 11:
        print(" Congratulations!", name, "You will be promoted, as a middle-class performer")
        Good_performers.append(name)
    else:
        print(" Please work harder next time!")
        Average_performers.append(name)

    resp = input("More staff? Enter 0 to quit:")
    if resp == "0" :
        break
    else:
        continue

print( "High Performers:", High_performers)
print( "Good Performers:", Good_performers)
print( "Average Performers:", Average_performers)

"""

"""
str = 'The rain in Spain falls mainly in the plane’
tokens = string.split(str)

str = 'The rain in Spain falls mainly in the plane’
tokens = string.split(str)

"""

"""
import string

token =["The", "rain", "in", "Spain", 'falls', 'mainly', 'in', 'the',  'plane']
str1 = " ".join(token)

print (str1)
str2 = str1
print (str2.split())

"""
"""

nums = [3, 41, 12, 9, 74, 15]
print (len(nums))
6
print (max(nums))
74
print (min(nums))
3
print (sum(nums))
154
print (sum(nums)/len(nums))
26

"""

"""
nums = [3, 41, 12, 9, 74, 15]
print (len(nums))
6
print (max(nums))
74
print (min(nums))
3
print (sum(nums))
154
print (sum(nums)/len(nums))
26tup1 = (12, 34.56); tup2 = ('abc', 'xyz');
tup3 = tup1 + tup2;
Print(tup3)

"""

"""
nums = [3, 41, 12, 9, 74, 15]
print (len(nums))
print (max(nums))
print (min(nums))
print (sum(nums))
print (sum(nums)/len(nums))

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)

"""

"""

print(tup3)newtuple = tuple('Hello World!')
 newtuple
('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')

"""

"""
#print (tup)cset = {11, 11, 22, 23, 24, 24, 11, 22, 25}



cset = {11, 11, 22, 23, 24, 24, 11, 22, 25}

num = [10,20,30,(10,20),40]
for i in num:
        if type(i)==tuple:
            print("Tuple found at" ,num.index(i))

"""

alist = [11, 22, 33, 22, 44]
aset = set(alist)
print ( aset)
{33, 11, 44, 22}
a = set(["Jake", "John", "Eric", "Mike"])
print(a)
b = set(["John", "Jill"])
print(b)
a = set(["Jake", "John", "Eric", "Mike"])
print(a)
b = set(["John", "Jill"])
print(b)
print(a.difference(b))
print(b.difference(a))
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))
print(a.union(b))
print(a.union(b))
print(a.symmetric_difference(b))

