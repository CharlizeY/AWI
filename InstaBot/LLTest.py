import sys
import csv
import time
import re
import requests
import instabot
from instabot import Bot

bot = Bot()
bot.login()
Users = bot.get_user_following("larrys_list")
bot.logout()

i = 0
url1 = 'https://i.instagram.com/api/v1/users/'
url3 = '/info'
UserNames = []
for user in Users:
    i = i + 1
    time.sleep(5)
    print('User ', i, ':', user)
    url2 = str(user)
    url = url1 + url2 + url3
    Req = requests.get(url)
    info = str(Req.text)
    name = re.search(r'username": "(.*?)",', info).group(1)
    try:
        print(name)
        UserNames.append(name)
    except:
        print("key error")

Followers = open("LLFollowingNames.csv", 'w')
wr = csv.writer(Followers, dialect='excel')
for name in UserNames:
    wr.writerow([name])
