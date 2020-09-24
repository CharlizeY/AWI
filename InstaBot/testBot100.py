import sys
import csv
import time
import json
import random
import instabot
from instabot import Bot

bot = Bot()
bot.login()

Messages = ["Hi", "Greetings", "Hello", "Heya", "Hey"]
Nice = [" nice ", " great "]

Users = bot.get_hashtag_users('dailymeditation')
Users = Users[0:50]

UserNames = []
print(Users, len(Users))
delay = 86400 / 100 # the rate which would allow 100 users per day 
print(delay/60)


for subgroup in Users:
    for user in subgroup:

        info = bot.get_user_info(user)
        username = info["username"]
        try:
            name = info["full_name"].split()[0]
        except:
            name = ""

        UserNames.append(username)
        index = random.randint(0, len(Messages)-1)
        greet = Messages[index]
        index2 = random.randint(0, len(Nice)-1)
        nice = Nice[index2]
        message = greet + " " + name + ", have a" + nice +  "day!"

        bot.send_message(message, username)
        print(username, message)

        time.sleep(delay + random.randint(0, 300))

# bot.logout()
