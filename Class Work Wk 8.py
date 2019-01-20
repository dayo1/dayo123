"""

a = range (1,50)
list1 =[]
for num in a:
    if num %2 != 0:
        list1.append(num)
print (list1)

"""
"""
a = range (1,20)
our_list =[]

for num in a:
    sqd_items = num **2
    our_list.append(sqd_items)

print (our_list)
"""

"""
list = ['physics', 'chemistry', 2000, 2018]
print ("Value available at index 2 : ", list[2])
list[2] = 2001
print ("Value available at index 2 : ", list[2])


list = ['physics', 'chemistry', 2000, 2018]
#print ("Value available at index 2 : ", list[2])
#list[2] = 2001
#print ("Value available at index 2 : ", list[2])
del list[2]
print(list)

"""

"""
list = ['physics', 'egg', 'chemistry', 2018, 2000, 2018, 2019, 2018]
print ("count for 2008 : ", list.count(2008))
print ("count for egg : ", list.count('egg'))

list = ['physics', 'egg', 'chemistry', 2018, 2000, 2018, 2019, 2018]
print ("count for 2018 : ", list.count(2018))
print ("count for egg : ", list.count('egg'))

"""

"""
list1 = ['physics', 'chemistry', 'maths', 1997, 2018, 2, ]
list2= list(range(7))
list1.extend(list2)
print (list1)

"""

"""
str1 = "9-Solutions"
cnt=0
list1=[]
for i in str1[0:]:
    if (cnt%2)!=0:
        cnt=cnt+1
    else:
        list1.append(i)
        cnt=cnt+1
print(list1)
print ("".join(list1))

"""

"""
horsemen = ["war", "famine", "pestilence", "death"]
i = 0
while i < 4:
    print (horsemen[i])
    i = i + 1

"""

"""
horsemen = ["war", "famine", "pestilence", "death"]
i = 0
while i < 4:
    print (horsemen[i])
    i = i + 1
    
    """

"""
x = [ "Alabama", "Alaska", "Arizona", "Arkansas", "California"]
y = [ "Colorado", "Florida"]

if y in x:
    print ("valid state")
else:
    print ("there are more states than listed")
    x.append(y)

print(x)

"""

"""
a = [1,2,[3,3],4,[5,6],7,["egg","none"]]

for i in a:
    if type(i) == type(a):
        print(i)
    else:
        print("false")

"""

"""
horsemen = ["war", "famine", "pestilence", "death"]
for horseman in horsemen:
    print (horseman)

"""

"""
list1 = ['physics', 'chemistry', 'maths']
list1.insert(1, 'Biology')
print ('Final list : ', list1)

"""

"""
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.pop()
print ("list now : ", list1)
list1.pop(1)
print ("list now : ", list1) 

"""

"""
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.reverse()
print ("list now : ", list1)


list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print ("list now : ", list1)

"""


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print ('Happy New Year:',  friend)
print ('Done!')