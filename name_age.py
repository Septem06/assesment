import random


def get_name():
    name_local = input("what is your name: ")
    return name_local
def get_age():
    age_local = int(input("how old are you: "))
    return age_local


#main routine
name = get_name() #1 function
age = get_age() #2 function
print(f"\nhi {name}. At {age} years old, you might find this a bit easy.\n"
      "\nanyway, this is a test about maori numbers. \n"
      "you will need to enter the number that applies\n"
      "e.g 1 for tahi or 2 for rua \n")

number = [["1", "tahi"], ["2", "rua"], ["3", "toru"]]

random.shuffle(number)

for i in number:
    answer = input(f"Enter the number which applies to {i[0]}: ")
    if answer == i[1]:
        print("##### correct! ####\n")
    else:
        print("xxxx incorrect xxxx")
