from tkinter import *
from pandas import *
import random
timer = None

def start_timer():
    global timer
    timer = window.after(3000, next_word, canvas.itemcget(current_title, "text"))

def next_word(language_type):
    global word_pair

    if language_type == "French":
        english_word = word_pair["English"]
        canvas.itemconfig(card_image, image=card_back)
        canvas.itemconfig(current_title, text="English", fill="white")
        canvas.itemconfig(current_word, text=english_word, fill="white")

    else:
        word_pair = random.choice(data)
        french_word = word_pair["French"]
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(current_title, text="French", fill="black")
        canvas.itemconfig(current_word, text=french_word, fill="black")


    start_timer()

def add_word_to_learn():
    global word_pair
    new_df = DataFrame([word_pair])
    file_path = "data/words_to_learn.csv"
    try:
        existing_df = read_csv(file_path)
        if not ((existing_df["French"] == word_pair["French"]) & (existing_df["English"] == word_pair["English"])).any():
            new_df.to_csv(file_path, mode='a', index=False, header=False)
        else:
            print("Word already in list")
    except FileNotFoundError:
        new_df.to_csv("data/words_to_learn.csv", mode='w', index=False, header=True)


try:
    data = read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = read_csv("data/french_words.csv").to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
current_title = canvas.create_text(400, 150, text="Get Ready", font=("Arial", 40, "italic"))
current_word = canvas.create_text(400, 263, text="Starting soon", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

correct_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, border=0)
correct_img = PhotoImage(file="images/right.png")
correct_button.config(image=correct_img)
correct_button.grid(row=2, column=1)

incorrect_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, border=0, command=add_word_to_learn)
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button.config(image=incorrect_img)
incorrect_button.grid(row=2, column=0)

word_pair = random.choice(data)
start_timer()

window.mainloop()
