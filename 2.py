import re
def match_string(s):
    pattern = r'a+bb?'
    if re.match(pattern, s):
        print("t")
    else:
        print("f")


s = input()
match_string(s)