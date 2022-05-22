import random

# this example uses two ordinary lists (1,D)

print("this is a test about numbers and what they are in maori.\n"
      "you will have to type the maori word for a number\n")

# 1st list
numbers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
# 2nd list(e_number meaning the english version)
e_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

question = random.choice(numbers)
attemt = input(f"what is abbreviation for {question}: ")

