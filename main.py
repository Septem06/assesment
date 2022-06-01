# This is what will check if you have play the game before


def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
        else:
            print("please answer 'yes' or 'no'")


import random



show_instructions = yes_no("have you played this game before? ")
def have_played(show_instructions):
    while True:
        answer = yes_no(print(f"you entered'{show_instructions}'"))
    if answer == yes_no('tell instructions')






name = "player1" #1 function
print(f"\nhi {name}. you might find this a bit easy.\n"
      "\nthis is a test about maori numbers. \n"
      "you will need to enter the number that applies\n"
      "e.g 1 for tahi or 2 for rua \n"
      "here is a practice for u \n")

number = [["tahi", "1"], ["rua", "2"], ["toru", "3"]]

random.shuffle(number)

for i in number:
    answer = input(f"Enter the number which applies to {i[0]}: ")
    if answer == i[1]:
        print("##### correct! ####\n")
    else:
        print("xxxx incorrect xxxx")


print("This is a test is about commonly used maori number. \n"
      "You will need to enter the abbreviation/ number which applies.")


# 1st list(this list
numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
           ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

choice = input("enter this letter to start: 'n' : ")
if choice == "n":
    choice = numbers


random.shuffle(choice)

for i in number:
    answer = input(f"Enter the number which applies to {i[0]}: ")
    if answer == i[1]:
        print("##### correct! ####\n")
    else:
        print("xxxx incorrect xxxx")


print()
having_fun = yes_no("Are you having fun? ")
print(f"you entered'{having_fun}'")
