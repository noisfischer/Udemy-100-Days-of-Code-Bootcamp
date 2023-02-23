import random
import replit


def next_guess(lives, number):
  
  guess = int(input("\nMake a guess: "))
  
  if guess == number:
    print(f"\nYOU WIN! The number was {number}, you guessed it right!\n")
    return
  elif guess < number:
    lives -= 1
    if lives == 0:
      print(f"\nYOU LOSE! You ran out of lives. The number was {number}.\n")
      return
    else:
      print(f"TOO LOW! The number is greater than {guess}.")
      print(f"You have {lives} attempts left.")
      next_guess(lives, number)
  elif guess > number:
    lives -= 1
    if lives == 0:
      print(f"\nYOU LOSE! You ran out of lives. The number was {number}.\n")
      return
    else:
      print(f"TOO HIGH! The number is less than {guess}.")
      print(f"You have {lives} attempts left.")
      next_guess(lives, number)
    
    next_guess(lives, number)
    


play_again = 'y'

while play_again != 'n':

  answer = random.randint(1,100)
  
  print("Welcome to the NUMBER GUESSING GAME!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  replit.clear()
  
  if difficulty == 'hard':
    num_attempts = 5
    print(f"\nYou have {num_attempts} attempts to remaining to guess the number.\n")
  else:
    num_attempts = 10
    print(f"\nYou have {num_attempts} attempts to remaining to guess the number.\n")
  
  next_guess(lives = num_attempts, number = answer)
  
  play_again = input("Play again? Type 'y' or 'n': ")
  replit.clear()


print("THANKS FOR PLAYING!")
