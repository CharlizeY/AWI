import sys
import requests
import bs4
import csv
from bs4 import BeautifulSoup

def findTags(URL):
    Req = requests.get(URL)
    soup = BeautifulSoup(Req.content, "lxml")

    for tag in soup.find_all('meta'):
        if(tag.get('property', None) == 'instapp:hashtags'):
                print(tag.get('content', None))

URLs = []
if (".csv" in sys.argv[1]):
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            URL = row[0]
            URLs.append(URL)
    for i in range(1, len(URLs)):
        findTags(URLs[i])
else:
    findTags(sys.argv[1])
