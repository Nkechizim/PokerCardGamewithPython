import re

pattern = re.compile("flower")

#the match method looks for a pattern at the beginning of a text
print(pattern.match("a beautiful flower power"))

match = pattern.match("flower power")

if match:
    print(match.start())
    print(match.end())
    print(match.span())
    print(match.group())