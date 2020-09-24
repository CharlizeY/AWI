import sys
import csv
import time
import json
import random
import instabot
from instabot import Bot

# log into your Ins account
bot = Bot()
bot.login()

Messages = ["Hi", "Greetings", "Hello", "Heya", "Hey"]
Nice = [" nice ", " great "]

Users = bot.get_hashtag_users('mindfulness')
UserNames = []
print(Users, len(Users))
delay = 86400 / 84


for user in Users:

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

    time.sleep(delay)

# bot.logout()
