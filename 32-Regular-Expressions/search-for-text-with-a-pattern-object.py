import re

pattern = re.compile("flower")
print(type(pattern))

#the search method looks for a pattern in an entire text
print(pattern.search("candy"))

print(pattern.search("beautiful flower"))
match = pattern.search("a beautiful flower in the field flower")
print(type(match))

if match:
    print(match.start())
    print(match.end())
    print(match.span())