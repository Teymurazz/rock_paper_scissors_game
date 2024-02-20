import random
import time
user_score = 0
comp_score = 0
while True:
    options = ["rock", "paper", "scissors"]
    user_win = ["rockscissors", "paperrock", "scissorspaper"]
    user_choice = input("Enter rock, scissors or paper:")
    comp_choice = random.choice(options)
    if user_choice not in options:
        print("Wrong Move!")
        continue
    if user_choice + comp_choice in user_win:
        print(f"Your choice is {user_choice}, and comp's choice is {comp_choice}")
        print("Proceeding....")
        time.sleep(1)
        print("You win")
        print("You", "Comp")
        user_score+=1
        print(f"{user_score}:    {comp_score}")
    elif user_choice == comp_choice:
        print(f"Your choice is {user_choice}, and comp's choice is {comp_choice}")
        print("Proceeding...")
        time.sleep(1)
        print("Tie")
    else:
        print(f"Your choice is {user_choice}, and comp's choice is {comp_choice}")
        print("Proceeding...")
        time.sleep(1)
        print("Comp win")
        print("You", "Comp")
        comp_score+=1
        print(f"{user_score}:   {comp_score}")
    if user_score == 10 or comp_score == 10:
        break
print("Game over.Thank you for enjoy!!!")
