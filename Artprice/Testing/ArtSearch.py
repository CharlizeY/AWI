import requests, sys, webbrowser, bs4

searchString = 'https://www.google.com/search?q='

s1 = 'Fine Art Sales'
s2 = 'Art Auction Houses'
s3 = 'Art and Sculpture Sales'

sList = s1, s2, s3


for i in sList:
    webbrowser.open(searchString + i)
