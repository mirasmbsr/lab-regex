import re

def match_string(string):
    pattern = r'a+b*'
    if re.match(pattern, string):
        print("T")
    else:
        print("F")

N = input()
match_string(N)