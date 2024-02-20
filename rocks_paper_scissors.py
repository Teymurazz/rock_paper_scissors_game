import random

user_score = 0
comp_score = 0
while True:

 options = ["rock", "scissors", "paper"]
 user_win = ["rockscissors", "scissorspaper", "paperrock"]
 user_choice = input("Enter scissors, paper or rock:")
 print(f"Your choice is {user_choice}")
 comp_choice = random.choice(options)
 print(f"Computer choice is {comp_choice}")
 if user_choice == comp_choice:
    print("Tie")
 elif user_choice + comp_choice in user_win: 
    print("You win")
    user_score+=1
    print(f"{user_score} {comp_score}")
 else: 
     print("Comp win")
     comp_score+=1
     print(f"{user_score} {comp_score}")
 if user_score == 10 or comp_score == 10:
   break
print("Game over")