import re
def upercase(s):
    pattern = "[A-Z]"
    return re.split(pattern, s)

print(upercase(input()))