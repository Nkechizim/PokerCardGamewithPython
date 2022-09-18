import collections

Book = collections.namedtuple("Book", ["title", "author"])

serendipity = Book("Serendipity", "Michelle")
even_now = Book("Even Now", "Michelle")

class Library():
    def __init__(self, *books):
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library(serendipity)
l2 = Library(serendipity, even_now)

print(len(l1))
print(len(l2))

class Newspaper():
    def __init__(self, pages, sections):
        self.pages = pages
        self.sections = sections
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        return self.pages == other.pages and len(self.sections) == len(other.sections)
    def __getitem__(self, index):
        return self.sections[index]
    def __setitem__(self, index, value):
        self.sections[index] = value