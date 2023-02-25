import random
from game_data import data
import replit

def random_selection():
  return random.randint(0, len(data) - 1)


try_again = 'y'

while try_again == 'y':
  print("Welcome to the Higher Lower game!\n")
  input("Press 'Enter' to start: ")
  
  replit.clear()
  
  #Assigns a random number for index of data list of dictionaries
  selectionA = random_selection()
  selectionB = random_selection()

  
  #GAME STARTS AND REPEATS HERE
  keep_playing = 'y'
  score = 0
  
  while keep_playing == 'y':
    
    #Assigns variables to the value of each key
    nameA = data[selectionA]['name']
    followersA = data[selectionA]['follower_count']
    descA = data[selectionA]['description']
    countryA = data[selectionA]['country']
    
    nameB = data[selectionB]['name']
    followersB = data[selectionB]['follower_count']
    descB = data[selectionB]['description']
    countryB = data[selectionB]['country']
    
    print(f"Compare A: {nameA}, a {descA}, from {countryA}.\n")
    print(f"Compare B: {nameB}, a {descB}, from {countryB}.\n")
    
    choice = input("Who do you think has more followers? Type 'A' or 'B': ").upper()
    
    if choice == 'A':
      if followersA > followersB:
        score += 1
        selectionB = random_selection()
        while selectionB == selectionA:
          selectionB = random_selection()
        replit.clear()
        print(f"You guessed right!\nSCORE = {score}\n")
      elif followersA < followersB:
        replit.clear()
        keep_playing = 'n'
    elif choice == 'B':
      if followersB > followersA:
        score += 1
        selectionA = random_selection()
        while selectionA == selectionB:
          selectionA = random_selection()
        replit.clear()
        print(f"You guessed right!\nSCORE = {score}\n")
      elif followersB < followersA:
        replit.clear()
        keep_playing = 'n'
    
    
  print("You guessed wrong!")
  try_again = input("Try again? Type 'y' or 'n': ")
  replit.clear()

print("THANKS FOR PLAYING!")