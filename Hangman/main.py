import random

from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#INTRO AREA
word_list = ["aardvark", "baboon", "camel", "moose", "sloth", "ostrich", "manatee", "iguana", "penguin"]

chosen_word = random.choice(word_list)

display = []

for x in chosen_word:
  display.append("_")

print(*display)
print(stages[-1])


#GAME START

stage_count = -2
guesses = []

while "_" in display and stage_count != -7:
  
  index = 0
  guess = input("Guess a letter: ").lower()
  clear()
  count = chosen_word.count(guess)

  if guesses.count(guess) != 0:
    print(f"You've already guessed {guess}. Try a different letter!")

  elif count == 0:
    print(stages[stage_count])
    print(f"{guess} is not in the word! You lose a life!")
    stage_count -= 1
    guesses += guess
    
  else:
    for x in chosen_word:
      if chosen_word[index] == guess:
        display[index] = guess
      index += 1

  print(*display)
  
  index = 0


#GAME END

print(stages[stage_count])

if stage_count == -7:
  print("YOU LOSE!")
else:
  print("YOU WIN!")