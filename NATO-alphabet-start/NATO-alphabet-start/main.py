import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    user_input = input("Write a prompt: ").upper()
    try:
        output = [dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()