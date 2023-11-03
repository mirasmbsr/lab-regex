import re

def splitprobel(s):
    pattern = r"[\sA-Z]"
    return re.split(pattern, s)

print(" ".join(splitprobel(input())))