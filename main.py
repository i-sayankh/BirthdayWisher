import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "sayank.khutia123@gmail.com"
MY_PASSWORD = "))142&wo"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for person in data_dict:
    if person["month"] == month and person["day"] == day:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
                content = file.read()
                content = content.replace("[NAME]", person["name"])

            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday\n\n{content}")

