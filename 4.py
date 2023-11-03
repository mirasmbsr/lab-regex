import re

def findbigpotomsmall(s):
    pattern = "[A-Z]+[a-z]*"
    if re.search(pattern, s):
        print("T")
    else:
        print("F")



s = input()
findbigpotomsmall(s)