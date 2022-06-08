
import random

print("This is a test about commonly used abbreviations. \n"
      "You will need to enter the abbreviation which applies "
      "e.g. Fri for Friday or 4 for April\n")


# Ist list

# 1st list
numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
           ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

choice = input("enter test: 'n' for numbers: ")
if choice == "n":
    choice = numbers

random.shuffle(choice)

for i in choice:
    answer = input("Enter the abbreviation which applies {}: ".format(i[0]))
    if answer == i[1]:
        print("#### correct ####\n")


