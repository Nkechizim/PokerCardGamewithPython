def vowel_count(string: str):
    return string.count("a") + string.count("e") + string.count("i")+string.count("o")+string.count("u")

print(vowel_count("estate"))        # => 3