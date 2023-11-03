import re

pattern = "[a-z]+_[a-z]*"

if re.search(pattern, input()):
    print("T")
else:
    print("F")

