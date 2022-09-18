import re

#in order to avoid creating a pattern object using the compile method, 
#the methods such as search, match, findall and findall are all directly available the re object, 
#you just have to provide two parameters, the first is the pattern and the second is the text

print(re.search("flower", "beautiful flower field"))
print(re.match("flower", "beautiful flower field"))
print(re.findall("flower", "beautiful flowery flower field"))