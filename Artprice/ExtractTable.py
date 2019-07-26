def ExtractTable(URL):

    import requests
    import bs4
    from bs4 import BeautifulSoup

    Req = requests.get(URL)
    soup = BeautifulSoup(Req.content, "lxml")
    Div = soup.find("div", {"id" : "infos"})

    def findRows(attribute, array):
        for tag in Div.find_all('td', attrs={'class': attribute}):
            array.append(tag.text)

    Parameters = []
    Values = []
    findRows('section', Parameters)
    findRows('value', Values)

    index = 0
    for param in Parameters:
        index = index + 1
        if("Size" in param):
            sizeIndex = index - 1
        if("Price" in param):
            priceIndex = index - 1
        if("Artist" in param):
            ArtistIndex = index - 1
        if("Title" in param):
            TitleIndex = index - 1
        else:
            continue

    Artist = Values[ArtistIndex]
    try:
        Title = Values[TitleIndex]
    except:
        Title = 'Untitled'

    Dimensions = Values[sizeIndex]
    DimSplit = Dimensions.splitlines()
    for line in DimSplit:
        if ("in" in line):
            SizeInches = line
        elif ("cm" in line):
            SizeCM = line
        else:
            continue

    try:
        Price = Values[priceIndex]
        PriceSplit = Price.splitlines()
        for line in PriceSplit:
            if ("$" in line):
                PriceDollars = line
            elif ("£" in line):
                PriceSterling = line
            else:
                continue
    except:
        Price = 'Unlisted'

        # CONDITIONAL RETURN FOR EVERY PARAMETER WITH CORRESPONDING TEST

    if (Price == 'Unlisted'):
        return(Artist, Title, SizeInches, SizeCM, Price)
    else:
        return (Artist, Title, SizeInches, SizeCM, PriceDollars, PriceSterling)
