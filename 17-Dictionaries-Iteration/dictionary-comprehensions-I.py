languages = ["Python", "Java", "C#"]
length ={language: len(language) for language in languages}
print(length)

length2 ={language: len(language) for language in languages if "t" in language}
print(length2)

word = "supercalifragilisticexpialidocious"
word_length = {letter: word.count(letter) for letter in word}
print(word_length)

word_length2 = {letter: word.count(letter) for letter in word if letter > "j"}
print(word_length2)