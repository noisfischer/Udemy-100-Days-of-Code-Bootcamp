import smtplib
import pandas as pd
import datetime as dt
import random

MY_EMAIL = "noahpythontesting@gmail.com"
PASSWORD = "rvbtzglfnhxbqdfg"

df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

letter_options = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

current_time = dt.datetime.now()

for birthday in birthdays:
    if current_time.month == birthday["month"] and current_time.day == birthday["day"]:
        chosen_letter = random.choice(letter_options)
        with open(chosen_letter, "r") as letter:
            content = letter.read()
            personalized = content.replace("[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # makes the connection secure
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday["email"],msg=f"Subject: Happy Birthday!\n\n{personalized}")





