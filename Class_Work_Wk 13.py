"""
fp = open("newfile.txt", "w")
fp.write( "Python is a great language.\r\nYeah its great!!\r\n");
fp.close()

"""

"""

fp = open("week13.txt", "w")
fp.write( "Python is a great language.\r\nIt contains robust, yet easy to understand syntax.\r\n");
fp.write( "Python is a great language.\r\nIt contains robust, yet easy to understand syntax.\r\n");

fp.close()


with open ("week13.txt", "r") as a:
    contents = a.read()
print (contents)

"""

"""
def InsuranceFunc():

    age = int(input (" Please enter your age: "))
    if (age < 25):
        rate = 3053.25
    elif (age >= 25) and (age < 65):
        rate = 2028.40
    else:
        rate = 755.30
    while (True):
        print (" Please enter your preferred plan: ")
        plan = input (" E for Economy, S for Standard or P for Premium: ")
        if plan == 'E':
            final_rate = rate * 1.15
            print("Annual ECONOMY insurance price: $", final_rate)
        elif plan == 'S':
            final_rate = rate * 1.7
            print("Annual STANDARD insurance price: $", final_rate)

        elif plan == "P":
            final_rate = rate * 2.12
            print("Annual PREMIUM insurance price: $", final_rate)
        else:
            if (plan == "E") or (plan == "S") or (plan == "P"):
                print ("Thank you")
                break
            else:
                continue
InsuranceFunc()

"""


"""
def InsuranceFunc():
    age = int(input(" Please enter your age: "))
    if (age < 25):
        rate = 3053.25
    elif (age >= 25) and (age < 65):
        rate = 2028.40
    else:
        rate = 755.30
    while (True):
        print(" Please enter your preferred plan: ")
        plan = input(" E for Economy, S for Standard or P for Premium: ")
        if plan == 'E':
            final_rate = rate * 1.15
            print("Annual ECONOMY insurance price: $", final_rate)
        elif plan == 'S':
            final_rate = rate * 1.7
            print("Annual STANDARD insurance price: $", final_rate)

        else:
            final_rate = rate * 2.12
            print("Annual PREMIUM insurance price: $", final_rate)

        if (plan == "E") or (plan == "S") or (plan == "P"):
            print("Thank you")
            break
        else:
            print("Wrong Choice!")
            continue


InsuranceFunc()

"""


"""
with open ("week13.txt", "r+") as f:
    newfile = f.read()
    print(newfile)


"""

"""
with open ("test1.txt", "a+") as a:
    str2 = " \n Another popular programming language is Java \n." \
        " Both have large areas of application \n. "\
            "While Java is Static in typing, Python is dynamic"
    contents = a.write(str2)
#print (contents)
with open("test1.txt", "r") as a:
    newfile = a.read()
print(newfile)

"""

"""
color = ['Blue','Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('text3.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)
content = open('text3.txt')
print(content.read())

"""

"""
import csv
def users():
    list1 =[]
    with open('users.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            list1.append(row)
    print (list1)

users()

"""


import csv
def home():
    with open('Homes.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            print(row)


home()



"""
import datetime
import csv

def borrowed_books():
    author = input(" Enter author's name: ")
    title = input(" Enter title of the book: ")
    ISBN = input(" Enter ISBN of the book: ")
    ID =   input(" Enter ID of the User: ")
    borwd_date = datetime.datetime.now()
    date_borrowed = borwd_date.strftime("%d-%m-%Y")
    with open('Borrowed_books.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([author, title, ISBN, ID, date_borrowed])
borrowed_books()


import csv
with open('Borrowed_books.csv', 'r+', newline='') as rd:
    reader = csv.reader(rd)
    for row in reader:
        print(row)

"""

"""

import datetime
import csv

def borrowed_books():
    author = input(" Enter author's name: ")
    title = input(" Enter title of the book: ")
    ISBN = input(" Enter ISBN of the book: ")
    ID =   input(" Enter ID of the User: ")
    borwd_date = datetime.datetime.now()
    date_borrowed = borwd_date.strftime("%d-%m-%Y")
    with open('Borrowed_books.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([author, title, ISBN, ID, date_borrowed])
borrowed_books()

"""

""" 
import csv
with open('Borrowed_books.csv', 'r+', newline='') as rd:
    reader = csv.reader(rd)
    for row in reader:
        print(row)
"""


"""

import csv
def add_users():
    ID = input("Enter users ID:")
    with open('users.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            if ID in row:
                print("User already available")
                break
            if ID not in row:
                books_borrowed = 0
                with open('users.csv', 'a+', newline='') as rd2:
                    writer = csv.writer(rd2)
                    writer.writerow([ID, books_borrowed])
                    print("Successfully Added with ID", ID)
                    break


add_users()

"""

"""
import csv
def home():
    with open('Homes.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            print(row)


home()

"""

