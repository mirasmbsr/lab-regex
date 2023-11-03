import re
def colondd(s):
    pattern = "[ ,.]"
    return re.sub(pattern, ":", s)

print(colondd(input()))