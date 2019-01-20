"""
event_a = ["Peters", "Mary", 'John', "Jerry", "Greg"]
event_b = ["Jill", "Jane", "Mary", "Gab", "Jerry", "Greg"]
a = set(event_a)
b = set(event_b)

not_attend = a.difference(b)
print (not_attend)


event_a = ["Peters", "Mary", 'John', "Jerry", "Greg"]
event_b = ["Jill", "Jane", "Mary", "Gab", "Jerry", "Greg"]
a = set(event_a)
b = set(event_b)

not_attend = b.difference(a)
print (not_attend)

"""

"""
name = input("Enter your name please: ")
amt = float(input("Please enter amount you wish to spend:- "))
years = int(input("Enter the number of years:- "))
intr = 3.9 *0.01
futVal= amt * ((1 + intr) ** years)
mthpay = futVal/(years*12)
print(futVal)
print(mthpay)

"""

"""
contacts = {'sum': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
print(contacts)

contacts = {'sum': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
contacts.pop ('rich')
print(contacts)

contacts = {'sum': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
contacts['bill'] = '234-765'
print(contacts)

"""

def personal_details():
    name, dob = "Solo", 1/2/1980

    address = "Upper Marlboro, MD, USA"
    print("Name: {}\nAge: {}\nDOB: {}".format(name, dob, ))

personal_details()
