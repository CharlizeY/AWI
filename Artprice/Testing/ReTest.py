import re

str = 'The prices of MANÉ-KATZ\n/ the artworks on the Marketplace'

print(str)

string = re.search('The prices of (.*?)\n', str).group(1)
print(string)
