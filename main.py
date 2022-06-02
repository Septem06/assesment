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



def havent_played(show_instructions):
    while True:
        answer = input(show_instructions).lower()
        if answer == "yes" or answer == "y":
            answer = "Yes"
            print("lets play")
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            print(f"\nthis is a test about maori numbers. \n"
                  "you will need to enter the number that applies\n"
                  "e.g 1 for tahi or 2 for rua \n")
            return answer
        else:
            print("please answer 'yes' or 'no'")


show_instructions = havent_played("have you played this game before")
print(f"you entered'{show_instructions}'")
print()


name = "player1" #1 function
print(f"here is a practice for u \n")

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

# wtpa = want to play again.
restart = 1
while restart != "x":
    input("press any key to start again, or x to exit.")
