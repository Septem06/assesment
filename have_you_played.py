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






show_instructions = yes_no("have you played this game before? ")
def have_played(show_instructions):
    while True:
        answer = yes_no(print(f"you entered'{show_instructions}'"))
    if answer == yes
