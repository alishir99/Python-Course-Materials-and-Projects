import pandas
import smtplib
import datetime as dt
import random

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
now= dt.datetime.now()
month =now.month
day = now.day
date_tuple = (month, day)
my_email = "pythonkobra01@gmail.com"
my_pass = "Abcd1234()"
if date_tuple in birthdays_dict:
    birthday_person = birthdays_dict[date_tuple]
    choice_letter = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open (choice_letter) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email, to_addrs="pythonkobra01@gmail.com",
                                msg=f"Subject: motivationn\n\n{contents}")



























# import random
# import smtplib
#
# # my_email = "python.kobra01@gmail.com"
# # password = "Abcd1234()"
# # with smtplib.SMTP("smtp.gmail.com") as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(from_addr=my_email,
# #                         to_addrs="shirzadali687@gmail.com",
# #                         msg="Subject:test\n\nthis is just an auto python email."
# #     )
#
# #----------------------------------date and time-----------------------
# import datetime as dt
# now = dt.datetime.now()
# today = now.weekday()
# print(today)
#
# #----------------------------------read data---------------------------
# quotes=[]
# with open("quotes.txt") as data_file:
#     data = data_file.readlines()
#
# if today==2:
#     print(random.choice(data))
