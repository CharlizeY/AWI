

class Artwork:
    Artist = 'Artist'
    Price = 'Price'

Names = ['Bob', 'James', 'Helen', 'Sam', 'Jess', 'Maria', 'Kat']
Price = 7 * ['£100']

def Assign(Artwork, Parameter):
    for param in Parameter:
        Artwork.Parameter = param
        print(Artwork.Parameter)

Assign(Artwork, Names)
Assign(Artwork, Price)
