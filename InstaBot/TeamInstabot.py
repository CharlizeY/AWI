import datetime
currentDT = datetime.datetime.now()
import sys
import csv
import time
import json
import random
import instabot
from instabot import Bot

bot = Bot()
bot.login()

#list of potential words with Monte Carlo simulation showing 180 unique messages per 200 generated
Greetings = ["Greetings ", "Hi ", "Hello "]
I = [", I am sure ", ","]
With = ["with "]
Frieze = ["FIAC ", "FIAC week "]
You = ["you would be "]
Thinking = ["thinking "]
About = ["about the prices of Art! I wanted to "]
Share = ["share ", "make you aware "]
That = ["that you can now "]
Use = ["use ", "employ "]
Tech = ["technology to "]
Evaluate = ["evaluate ", "determine the value of "]
Art = ["art ", "artworks "]
More = ["more accurately. Would love your "]
Views = ["views! ", "thoughts! "]
Sign = ["ArtWorldInsights"]


Users = []
with open('IG3.csv') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   for row in csv_reader:
       Users.append([row[0], row[1]])


Users=list(map(list, zip(*Users)))
name=(Users[0])
username=(Users[1])

greetings = Greetings[random.randint(0, len(Greetings)-1)]
i = I[random.randint(0, len(I)-1)]
withArt = With[random.randint(0, len(With)-1)]
frieze = Frieze[random.randint(0, len(Frieze)-1)]
you = You[random.randint(0, len(You)-1)]
thinking = Thinking[random.randint(0, len(Thinking)-1)]
about = About[random.randint(0, len(About)-1)]
share = Share[random.randint(0, len(Share)-1)]
that = That[random.randint(0, len(That)-1)]
use = Use[random.randint(0, len(Use)-1)]
tech = Tech[random.randint(0, len(Tech)-1)]
evaluate = Evaluate[random.randint(0, len(Evaluate)-1)]
art = Art[random.randint(0, len(Art)-1)]
more = More[random.randint(0, len(More)-1)]
views = Views[random.randint(0, len(Views)-1)]
sign = Sign[random.randint(0, len(Sign)-1)]

Delay= 86400 / 20
bot.max_followers_to_follow=500000
bot.max_followers_to_following_ratio=10000

for j in range(0, len(name)):
  Message = greetings + str(name[j]) + i + withArt + frieze + you + thinking + about + share + that + use + tech + evaluate + art + more + views + sign
  try:
      bot.send_message(Message, username[j])
      print(Message)
      RandomDelay = Delay + random.randint(0, 300)
      time.sleep(RandomDelay)
      print(RandomDelay)
      print(str(currentDT))
  except TypeError:
      continue


bot.logout()
