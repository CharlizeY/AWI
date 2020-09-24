import csv
import time
import random
import instabot
from instabot import Bot

bot = Bot()
bot.login()

unfollowUsers = []
with open("unfollow.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        unfollowUsers.append(row[0])

for user in unfollowUsers:
    time.sleep(random.randint(60, 300))
    bot.unfollow_users(user)
