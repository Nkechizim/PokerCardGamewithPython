print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "apples"])

print([num/2 for num in range(21)])

donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]

creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)

print([len(donut) for donut in donuts if "Cream" in donut])

print([donut.split(" ") for donut in donuts if "Cream" in donut])
print([donut.split(" ")[0] for donut in donuts if "Cream" in donut])

def destroy_elements(list1, list2):
    new_list = [num for num in list1 if num not in list2]
    return new_list

print(destroy_elements([1, 2, 3], [1, 2]))