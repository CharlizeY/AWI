import requests
import csv
import sys
import bs4
from bs4 import BeautifulSoup
from ExtractTable import ExtractTable

URLs = []
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        ArtURL = row[0]
        URLs.append(ArtURL)

for url in URLs:
    Results = ExtractTable(url)
    for result in Results:
        print(result)
# Results = ExtractTable('https://www.artprice.com/marketplace/13801/henry-charles-fox/painting/untitled')
# for result in Results:
#     print(result)
