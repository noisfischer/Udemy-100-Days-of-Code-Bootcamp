import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Write a prompt: ").upper()
letters = [letter for letter in user_input]
result = []
for letter in letters:
    if letter in dict:
        result.append(dict[letter])
print(result)