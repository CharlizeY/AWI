import sys
import csv
import time
import json
import requests
import instabot
from instabot import Bot

bot = Bot()
bot.login()
Users = bot.get_user_following("larrys_list")

i = 0
url1 = 'https://i.instagram.com/api/v1/users/'
url3 = '/info'
UserNames = []
for user in Users:
    i = i + 1
    time.sleep(10)
    print('User ', i, ':', user)
    url2 = str(user)
    url = url1 + url2 + url3
    Req = requests.get(url)
    html = str(Req.text)
    info = json.loads(html)
    name = info["user"]["username"]
    try:
        print(name)
        UserNames.append(name)
    except:
        continue

Followers = open("LLFollowingNames.csv", 'w')
wr = csv.writer(Followers, dialect='excel')
for name in UserNames:
    wr.writerow([name])
