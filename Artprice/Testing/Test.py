import csv
import requests

def reqURL(url):
    R = requests.get(url)
    print(R)

with open('Test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        ArtURL = str(row[0])
        print(ArtURL)

        requests.get(ArtURL)
        # print(url)
