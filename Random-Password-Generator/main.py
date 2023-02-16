#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

all_characters = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for x in range(0, nr_letters):
#   letter = random.randint(0, len(letters) - 1)
#   x = letters[letter]
#   print(x, end="")
# for x in range(0, nr_numbers):
#   number = random.randint(0, len(numbers) - 1)
#   x = numbers[number]
#   print(x, end="")
# for x in range(0, nr_symbols):
#   symbol = random.randint(0, len(symbols) - 1)
#   x = symbols[symbol]
#   print(x, end="")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letter_r = [] #Create a new list of letters using the specified number of letters the user wants

for x in range(0, nr_letters):
  letter = random.randint(0, len(letters) - 1)
  x = letters[letter]
  letter_r.append(x)

number_r = [] #Create a new list of numbers using the specified number of letters the user wants

for x in range(0, nr_numbers):
  number = random.randint(0, len(numbers) - 1)
  x = numbers[number]
  number_r.append(x)

symbol_r = [] #Create a new list of symbols using the specified number of letters the user wants
  
for x in range(0, nr_symbols):
  symbol = random.randint(0, len(symbols) - 1)
  x = symbols[symbol]
  symbol_r.append(x)

list_length = nr_letters + nr_numbers + nr_symbols #total number of indeces in all lists

final_list = []

final_list.extend(number_r)
final_list.extend(letter_r)
final_list.extend(symbol_r) #Created a single list with all randomly generated characters

final_list = random.sample(final_list, list_length) #randomly selects characters from our final list without duplicates however many times our list_length is

print(''.join(final_list)) #converts the new version of final_list to a string with no spaces and prints the result



  
