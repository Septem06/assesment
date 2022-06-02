def havent_played(show_instructions):
    while True:
        answer = input(show_instructions)
        if answer == "yes" or answer == "y":
            answer = "Yes"
            print("lets play")
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            print("this game is made to test you on the maori numbers")
            return answer
        else:
            print("please answer 'yes' or 'no'")


show_instructions = havent_played("have you played this game before")
print(f"you entered'{show_instructions}'")
print()
