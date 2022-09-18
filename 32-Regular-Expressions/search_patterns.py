#   \w any letter from a-z upper or lower case including digits and _
#   \W any non-letter character such as whitespace, commas, periods, $% etc.
#   \s any whitespace character in a text including line breaks
#   \S any non-whitespace character in a text
#   \b a word boundary: 
#       if at the beginning of a word/text it searches for the pattern at the beginning
#       if at the end of a word/text it searches for the pattern at the end
#   \B a word boundary: 
#       if at the beginning of a word/text it searches for the pattern that is NOT at the beginning
#       if at the end of a word/text it searches for the pattern that is NOT at the end
#   metacharacters: characters that have their own meaning in regular expression
#     . any character at all excluding a line break (*use a backslash to escape metacharacters)
#     []with character inside --> this searches for each of the characters in the bracket not in sequence
#     [^]with character inside --> this searches for characters except the ones in the bracket
#     [a-l] --> this searches for characters within the range (*it is case sensitive)
#   z{3} three(any number) ocurrences of a character in a row (in this case z)
#   z{3,} three or more(any number) ocurrences of a character in a row (in this case z)
#   z{3,6} between three and six(any numbers) ocurrences of a character in a row (in this case z)
#   a+ one of more of a character
#   a* zero of more of a character
#   (a|b) search for one character or another

#   \d{3}-\d{3}-\d{4} three digits in a row, a dash, three digits in a row, a dash, four digits in a row
#   \d{3}\s\d{3}\s\d{4} three digits in a row, a space, three digits in a row, a space, four digits in a row
#   \d{3}\s{1,}\d{3}\s{1,}\d{4} three digits in a row, any number of space, three digits in a row, any number of space, four digits in a row
#   \d{3}\s+\d{3}\s+\d{4} three digits in a row, any number of space, three digits in a row, any number of space, four digits in a row