import re 

def adob(s):
    pattern = "^a.*b$"
    if re.search(pattern, s):
        print("T")
    else:
        print("F")

s = input()

adob(s)