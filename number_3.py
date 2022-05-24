import random

print("This is a test about commonly used abbreviations. \n"
      "You will need to enter the abbreviation which applies "
      "e.g. Fri for Friday or 4 for April\n")


# Ist list

# 1st list
numbers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
# 2nd list(e_number meaning the english version)
e_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

choice = input("enter test: 'n' for numbers: ")
if choice == "n":
    choice = e_number
else:
    choice = numbers


random.shuffle(choice)

for i in choice:
    answer = input("Enter the abbreviation which applies {}: ".format(i[0]))
    if answer == i[1]:
        print("#### correct ####\n")

    else:
        print("xxxx incorrect xxxx\n")
