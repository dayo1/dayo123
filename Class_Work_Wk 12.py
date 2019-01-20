
"""
Empl = {"John Robson": 7, "Bill Gates": 10, "Steve Jobs": 20, "Ben Royce": 16,
        "Mike Thompson":3, "peter Hen": 9, "Sam Peterson": 21,
        "Bet Johnson": 21, "Michael Clairs": 4, "Glen Becks": 18}

print("Total service year by all employees:", sum(Empl.values()))
print("Employee with the highest no. of years: ", max (Empl.items (), key=lambda k:k[1]))
print("Employee with the least no. of years: ", min (Empl.items (), key=lambda k:k[1]))
print("Average no. of years: ", (sum(Empl.values())/len(Empl)))

"""

"""

def multiply (List):
    my_list=[]

    for n in List:
        result=n**3
        my_list.append(result)
    print(my_list)
    return
List1=range(1,30)
multiply(List1)

"""

"""
def ExponFunc ():
    list1 = range (1,30)
    list2 = []
    for item in list1:
        item= item**3
        list2.append(item)
    print(list2)
    return

ExponFunc()

"""

"""
def compare_temp(today):
    Spr_Avg = 68
    Sum_Avg = 95
    Fa_Avg  = 72
    Win_Avg = 42

    season = input ("Please enter S for summer, P for spring, F for fall "
                    "and W for winter:")

    if season == 'S':
        if (today - Sum_Avg > 5):
            return "It is hotter than usual."
        elif (today- Sum_Avg < -5):
            return  "It is colder than usual."
        else:
            return "The weather looks normal."


    elif season == 'P':
        if (today - Spr_Avg > 5):
            return "It is hotter than usual."
        elif (today- Spr_Avg < -5):
            return  "It is colder than usual."
        else:
            return "The weather looks normal."


    elif season == 'F':
        if (today - Fa_Avg > 5):
            return "It is hotter than usual."
        elif (today- Fa_Avg < -5):
            return  "It is colder than usual."
        else:
            return "The weather looks normal."


    elif season == 'W':
        if (today - Win_Avg > 5):
            return "It is hotter than usual."
        elif (today- Win_Avg < -5):
            return  "It is colder than usual."
        else:
            return "The weather looks normal."

    else:
        return "Wrong Season."

print(compare_temp(40))

"""


"""
import sys

player1 = input("Your name please?: ")
player2 = input("Enter the name of the second player please: ")

Play1_ans = input("Select an output: stone, spread or scissors: ")
Play2_ans = input("Select an output for the second player: Stone, Spread or Scissors: ")

def game_compare(s1,s2):
    if s1 == s2:
        return ('this is a tie')
    elif s1 == 'stone':
        if s2 == 'scissors':
            return ("stone wins")
        else:
            return ("spread wins")

    elif s1 == 'scissors':
        if s2 == "spread":
            return ("scissors wins!")
        else:
            return ("stone wins!")
    elif s1 == "spread":
        if s2 == 'stone':
            return  ('spread wins')
        else:
            return ('scissors wins')
    else:
        return ("Invalid selection! Please try again")
    sys (exit)

print(game_compare(Play1_ans, Play2_ans))

"""


"""
str = input("Your input please: ")
print("Received input is : ", str)

"""

"""
 Using a loop:
for i in a:
    print (i)

print("Name of the file: ", myfile.name)
print ("Closed or not: ", myfile.closed)
print("Opening mode : ", myfile.mode)

"""

"""
With open ("test1.txt", "r") as a:
    a.contents = a.read()
    print (a.contents)

"""

with open("text2.txt", "r") as myfile:
    contents = myfile.read()
    print(contents)



