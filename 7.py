import re

def snakecamel(s):
    w = re.split('_', s)
    u = w[0].capitalize()
    c = u + ''.join(word.capitalize() for word in w[1:])
    print(c)

s = input()
snakecamel(s)