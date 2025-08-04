import random

guess = random.randint(1,100)
tries = 0
print("🎮 Welcome to the Random Number Guessing Game! (Range: 1 to 100)")
while True:
       num = int(input("👉 Guess your number: "))
       tries += 1
       if num < 1 or num > 100:
        print("❌ Please guess a number between 1 and 100.")
        continue

       if guess==num:
             print("🎉 Congrats! You guessed the correct number!")
             print(f"🏆 You won the game in {tries} tries.")
             break
       elif num>guess:
            print("📉 Too high! Try again.")
            
       elif num<guess:
            print("📈 Too low! Try again. ") 
                   
