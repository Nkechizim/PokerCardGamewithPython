import re

#\d represents any digit in a text from 0-9
pattern = re.compile(r"\d")

sentence = "I went to the market and bought 5 apples, 4 oranges, and 15 plums"

print(pattern.findall(sentence))


#\D represents any  non-digit in a text
pattern = re.compile(r"\D")

sentence = "I went to the market and bought 5 apples, 4 oranges, and 15 plums"

print(pattern.findall(sentence))

#regex101.com