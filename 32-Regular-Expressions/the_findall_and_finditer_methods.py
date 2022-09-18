import re

pattern = re.compile("flower")

sentence = "There are a lot of flowers in the flowery flower field"

#findall returns a list with all the matches in string form
print(pattern.findall(sentence))
print(pattern.findall("Nonsense"))

#finditer returns a iterable of all the matches in match object form
for match in pattern.finditer(sentence):
    print(match)