empty_space = "     happy girl     "

print(empty_space.lstrip()) #removes the beginning spaces on the left side of a string
print(empty_space.rstrip()) #removes the ending spaces on the right side of a string
print(empty_space.strip()) #removes the spaces on both sides of a string

print()

website = "www.python.org"

print(website.lstrip("w"))
print(website.rstrip("org"))
print(website.strip("w.org"))

print()

print(website.replace(".", "-")) #replace a substring with a new substring

def fancy_cleanup(text: str):
   new_text = text.strip().replace("g", "z").replace(" ", "!")
   return new_text

print(fancy_cleanup("       geronimo crikey  "))