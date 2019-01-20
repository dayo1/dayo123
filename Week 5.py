
"""
word = input('please enter your word')
if word
"""



"""
Myfruit
 = 'apple'
print(len(Myfruit))
"""

"""
wrd = input ("Please enter a word: ")
rvs= wrd[::-1]
if wrd == rvs:
    print( "Your word ",wrd, " is a palindrome")
else:
    print("Your word ", wrd, " is not a palindrome")

    str1 = "programming"
    str2 = input(" Please enter a number: ")
    # slice programing to get program
    str3 = str1[0:7]
    print("str1[0:7] = ", str3)
    # str4 = str2 - 25
    str4 = int(str2) - 25
    print(" int(str2) - 25: = ", str4)
    
    """


"""
str1 ="please do not throw sausage pizza away, please do not , please !!"
str2 = "the quick brown fox jumps over the lazy "
str1= str1.split()
str2= str2.split()
counts = dict()
for word in str1: #str2:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print (counts)


greet = 'Hello Bob'
new = greet.replace('Bob','Jane')
print (new)

print (new)
lw = greet.lower()
print (lw)
lw = greet.lower()
print (lw)

greet = 'Hello Bob'
new = greet.replace('o','X')
print (new)


print (new)
lw = greet.lower()
print (lw)
lw = greet.lower()
print (lw)

"""

"""
greet = '   Hello Bob  '
new = greet.lstrip()
print(new)
greet = '   Hello Bob  '
new = greet.rstrip()
print(new)
new = greet.strip()

print(new)
"""

"""
Mystr = "Python is awesome....yeah!!!"
print("Padded string : ",Mystr.zfill(40))
print ("Padded String : ",Mystr.zfill(50))

"""

"""
str = "this is 2018"
print (str.isdecimal())
str = "23443434"
print (str.isdecimal())
line = 'Do have a nice day'
line.startswith('Do')
"""

"""
line = 'Do have a nice day'
line.startswith('Do')

"""

"""
dogs = 42
print('I have spotted %d dogs.' % dogs)

"""

"""
marks = int(input("Enter the score: "))

if (marks>80):
   print("Grade A")
elif (marks >60) and (marks<=80):
   print ("Grade B")
elif (marks>40) and (marks <=60):
   print ("Grade C")
else:
   print ("Grade D")


x = int(input("Enter the first number: "))
y = int(input("Please enter the second number: - "))

if (x==y) or abs(x-y) == 10:
    print("true")
else:
    print("false")
"""

"""
x = input("Enter a number: ")

if x.isdigit():
    print("processing. Please wait...")
else:
    print("Wrong input")


x = input("Enter a number: ")

if x.isdigit():
    print("Inputs are numbers...")
else:
    print("Wrong input")

"""
# line.startswith('Please')
dogs =42
print('I have spotted %d dogs.' % dogs)
str ='In %d years, I have spotted %g %s.' % (3, 0.1, 'dogs')
print(str)
