"""
card = input("Please enter the card number: ")
if len(card) == 16:
    print("Valid  card")
    if card.startswith('4'):
        print("this is a Visa card")
    elif card.startswith("51"):
        print("This is a Master Card")
    elif card.endswith("62"):
        print("Probably a discover card")
else:
    print("Invalid  card")

    """

"""
ft = int(input ("please enter the distance: "))
d_inches = ft * 12
d_yards = ft / 3.0
d_miles = ft / 5280.0
print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)

"""

"""
import string

psw = input('Enter a password to validate: ')
spec_chars = list()
upper = list()

for letter in psw:
    if letter.isupper():
        upper.append(letter)
    if letter in string.punctuation:
        spec_chars.append(letter)

if (len(psw) >= 6) and (len(psw) <= 8) and\
    (len(spec_chars) >= 1) and (len(upper) >= 1) :
    print('Valid Password!')
else:
    print('Invalid Password')

"""

"""
import sys

player1 = input('Your name please?: ')
Player2 =  input("Enter of the second player please: ")

Play1_ans = input("Select an output: Stone, Spread or Scissors: ")
Play2_ans = input("Select an output for the second player: Stone, Spread or Scissors: ")


def game_compare(s1,s2):
    if s1 == s2:
        return ('this is a tie')
    elif s1 =='stone':
        if s2 == 'scissors':
            return ("Stone wins")
        else:
            return("Spread wins")

    elif s1 == "scissors":
        if s2 == "spread":
            return("Scissors wins!")
        else:
            return ("Stone Wins!")

    elif s1 == "Spread":
        if s2 == 'stone':
            return ('Spread wins')
        else:
            return ("Scissors wins")

    else:
        return ("invalid selection! Please select again")
    sys(exit)

print(game_compare(Play1_ans, Play2_ans))

"""

"""
s1 = input("Select an output: Stone, Spread or Scissors: ")
s2 = input("Select an output for the second player: Stone, Spread or Scissors: ")

if s1 == s2:
    print('this is a tie')
elif s1 =='stone':
    if s2 == 'scissors':
        print ("Stone wins")
    else:
            print("Spread wins")

elif s1 == "scissors":
    if s2 == "spread":
         print("Scissors wins!")
    else:
        print ("Stone Wins!")

elif s1 == "Spread":
    if s2 == 'stone':
        print ('Spread wins')
    else:
            print ("Scissors wins")

else:
        print ("invalid selection! Please select again")

"""

"""
def compute_HolsPay():
    basic_pay = 2000.0

    level = input (" Please enter M for management, S for Senior, or J for Junior: ")
    if level == 'M':
        basic_sal = float(input("Enter management's basic salary: "))
        pay = (0.15 * basic_sal) + basic_pay +basic_sal
        return pay
    elif level == 'S':
        basic_sal = float(input("Enter Senior Cadre's basic salary: "))
        pay = (0.10 * basic_sal) + basic_pay + basic_sal
        return pay
    elif level == 'J':
        basic_sal = float(input("Enter Junior Cadre's basic salary: "))
        pay = (0.05 * basic_sal) + basic_pay + basic_sal
        return pay
    else:
        return"Wrong input."

print(compute_HolsPay())

"""

"""
import random

count = 0
while (count < 10):
    rand = random.random()
    print ( count + rand)
    count+= 1

"""

"""
for egg in range(100,0,-1):
    if egg>1:
        print(egg," eggs remaining in the crate")
    elif egg == 1:
        print("oops! only 1 egg is remaining")
    else:
        print("no more eggs!!!")

"""

"""
num =0
for num in range(15):
    num = num + 1
    if num == 8:
        break

    print("Number is = " + str(num))
print("Im out of loop")

"""

"""
num =0
for num in range(15):
    num = num + 1
    if num == 8:
        continue

    print("Number is = " + str(num))
print("Im out of loop")

"""

"""
num =0
for num in range(15):
    if (num % 2) == 0:
        continue

    print(num)

"""

"""
num =0
for num in range(15):
    if (num % 2) == 0:
        break

    print(num)

"""

#num =4
for num in range(9):
    if (num % 3) == 0:
        continue

    print(num)