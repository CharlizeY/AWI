from ExtractTableHTML import ExtractTableHTML
import csv
import sys

URLs = []
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        URL = row[0]
        URLs.append(URL)

Listings = []
for i in range(1, len(URLs)):
    Listings.append(ExtractTableHTML(URLs[i]))

MarketplaceData = open("MarketplaceData.csv",'w')
wr = csv.writer(MarketplaceData, dialect='excel')
wr.writerow(['Artist', 'Type', 'Title', 'Year', 'Category', 'Medium', 'Signature', 'Size', 'Certificate', 'Invoice', 'Condition', 'Ad', 'Price'])

for listing in Listings:
    row = []
    for name, value in listing.items():
        row.append(str(value))
    wr.writerow(row)
