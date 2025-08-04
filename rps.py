import random

print(f"Welcome To R-P-S Game \n      Rock\n      Paper\n     Scissor")
player_wins = 0
computer_wins = 0
draw = 0
round = 0 

while True:
    player = input("Enter Your Choice = ").lower()
    
    if player == "exit":
        print("👋 Thanks for playing!")
        print("\n   📊 Game Summary")
        print(f"🏆 You won     : {player_wins} times")
        print(f"💻 Computer won: {computer_wins} times")
        print(f"🤝 Draws       : {draw} times")
        print(f"🎯 Total Rounds: {round}")

        break
    if player not in ["rock", "paper", "scissor"]:
        print("❌ Invalid choice! Please choose rock, paper, or scissor.")
        continue
    round += 1
    computer = random.choice(["rock","paper","scissor"])
    if player == computer:
        result = "Draw"
        draw += 1
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
            result = "🎉 You Win🏆 !, Play..."
            player_wins += 1
    else:
        result = "💻 Computer Wins! Try again...."
        computer_wins += 1


    print(f"You chose {player.capitalize()}, computer chose {computer.capitalize()} → {result}") 
    print(f"You Wins {player_wins} Times\nComputer Wins {computer_wins} Times\n Total Draws {draw} Times\nTotal Rounds {round}")   



        
            