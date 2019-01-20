"""
fund = 100000.0

level = input (" Please enter  S for Senior, or J for Junior, SH for Sophomore or F for Freshmen: ")
CGPA = float(input("Enter your grade: "))

if level == 'S':
    if CGPA >= 3.5:
        pay = (0.37 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.24 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.26 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'J':
    if CGPA >= 3.5:
        pay = (0.33 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.33 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.33 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
"""
"""
fund = 100000.0

level = input (" Please enter  S for Senior, or J for Junior, SH for Sophomore or F for Freshmen: ")
CGPA = float(input("Enter your grade: "))

if level == 'S':
    if CGPA >= 3.5:
        pay = (0.37 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.24 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.26 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'J':
    if CGPA >= 3.5:
        pay = (0.33 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.33 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.33 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)

elif level == 'SH':
    if CGPA >= 3.5:
        pay = (0.26 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.26 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.26 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'F':
    if CGPA >= 3.5:
        pay = (0.33 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.33 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.33 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
else:
    print ("Wrong Level")

"""

"""
fund = 100000.0

level = input (" Please enter  S for Senior, or J for Junior, SH for Sophomore or F for Freshmen: ")
CGPA = float(input("Enter your grade: "))

if level == 'S':
    if CGPA >= 3.5:
        pay = (0.37 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.24 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.24 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'J':
    if CGPA >= 3.5:
        pay = (0.24 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.24 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.24 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'SH':
    if CGPA >= 3.5:
        pay = (0.26 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.26 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.26 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'F':
    if CGPA >= 3.5:
        pay = (0.33 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.33 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.33 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
else:
    print ("Wrong Level")
    
    """

"""
x = [1, 5, ‘physics’, ’apple’, [2,3]]mylist = list()-----\mylist = list()mylist = list()--
--
"""

"""
mylist = list()
mylist.append('book')
mylist.append(99)
mylist.append ('9solutions')
print(mylist)
# mylist.del[99]
print(mylist)

list1 = [1, 5, 'physics', 'apple', [2,3], 10]
print (list1[-1])


a = [5, 4, 3, 2, 1]
for y in a:
    print (y)
    print ("I’m done!")

"""

odds = [str(x) for x in range(50) if x%2 == 1]
print("Odds\n" + "\n".join(odds))