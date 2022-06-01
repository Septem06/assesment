import random

print("This is a test is about commonly used maori number. \n"
      "You will need to enter the abbreviation/ number which applies.")


# 1st list(this list
numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
           ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

choice = input("enter this letter to start: 'n' : ")
if choice == "n":
    choice = numbers


random.shuffle(choice)

for i in choice:
    answer = input("Enter the abbreviation which applies {}: ".format(i[0]))
    if answer == i:
        print("#### correct ####\n")

    else:
        print("xxxx incorrect xxxx\n")
