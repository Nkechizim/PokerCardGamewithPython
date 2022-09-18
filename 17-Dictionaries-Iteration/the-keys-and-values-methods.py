chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Rib": 7.99,
    "Fried Rice": 1.99
}

#the key and value method does not return a list but a dict_view object 
#and they're iterable
print(chinese_food.keys())
print(type(chinese_food.keys()))
print(chinese_food.values())
print(type(chinese_food.values()))

for food in chinese_food.keys():
    print(food)

for price in chinese_food.values():
    print(price)

def count_of_value(my_dict, num):
    count = [value for value in my_dict.values()]
    return count.count(num)

my_dict = { "a" : 5, "b" : 3, "c" : 5 }
print(count_of_value(my_dict, 5))