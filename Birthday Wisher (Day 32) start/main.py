import smtplib
import datetime as dt
import random

MY_EMAIL = "noahpythontesting@gmail.com"
PASSWORD = "rvbtzglfnhxbqdfg"

with open("quotes.txt") as quotes_data:
    quotes = quotes_data.readlines() # splits the quotes into a list per quote
    chosen_quote = random.choice(quotes)

current_time = dt.datetime.now() # gets current date and time (in local timezone)
# year = current_time.year    # returns the year as an int
# month = current_time.month  # returns the number month
# day = current_time.day  # returns the number day in the month
# day_of_week = current_time.weekday() # gives the day of the week as an int

if current_time.day == 0:   # If it's Monday
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # makes the connection secure
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="noahpythontesting@yahoo.com", msg=f"Subject:Monday Motivation\n\n{chosen_quote}")


