#this is used to change existing item in a list but not to add new items to the end
books = ["Welcome to Serenity", "This Lullably", "Even Now", "The Long Road Home"]
print(books)

books[0] = "The Other Woman"
print(books)

books[-1] = "Sacred"
print(books)

books[2:] = ["Welcome to Serenity", "Even Now", "Lost Love"]
print(books)