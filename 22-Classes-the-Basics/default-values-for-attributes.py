class Book():
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price


animal_farm = Book("The Animal Farm", "George Orwell")
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", 19.99)

print(animal_farm.price)
print(gatsby.price)