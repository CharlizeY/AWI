import sys
import csv
import time
import json
import requests
# import instabot
# from instabot import Bot

Users = []
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        for col in row:
            try:
                col = int(col[2:-1]) #have converted User ID to integer
            except:
                continue
            Users.append(col)
i = 0
url1 = 'https://i.instagram.com/api/v1/users/'
url3 = '/info'
Names = []
for user in Users:
    print('User ', i, ':', user)
    url2 = str(user)
    url = url1 + url2 + url3
    Req = requests.get(url)
    html = str(Req.text)
    info = json.loads(html)
    print(info["user"]["username"])
    Names.append(info["user"]["username"])
    i = i + 1
    time.sleep(0.25)

Followers = open("FollowerNames.csv", 'w')
wr = csv.writer(Followers, dialect='excel')
for name in Names:
    wr.writerow([name])
