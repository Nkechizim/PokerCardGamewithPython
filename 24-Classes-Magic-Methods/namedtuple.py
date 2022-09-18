import collections
#Book is a class but it also has characteristics of a tuple

Book = collections.namedtuple("Book", ["title", "author"])
#Book = collections.namedtuple("Book", "title author")

serendipity = Book("Serendipity", "Michelle")
print(serendipity)

print(serendipity[0])
print(serendipity[1])
print(serendipity.title)
print(serendipity.author)