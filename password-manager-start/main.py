#Password Generator Project
import random
from tkinter import *
from tkinter import messagebox

def save_entry():
  website_text = website_entry.get()  # get text in entry fields
  user_text = user_entry.get()
  pass_text = pass_entry.get()

  if len(website_text) == 0 or len(pass_text) == 0:
    messagebox.showinfo(title="Error", message="You left some fields empty!")
    return

  save = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {user_text} \n Password: {pass_text} \n Is it ok to save?")

  if save:
    with open("passwords.txt", "a") as passwords_file:  # "a" opens the file in 'append' mode
      passwords_file.write(f"{website_text} | {user_text} | {pass_text}\n")

    website_entry.delete(0, END)  # clear entry fields
    pass_entry.delete(0, END)

  print("Entry added to passwords.txt!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, width=500, height=500)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "noisfischer@gmail.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
