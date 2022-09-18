def sum_of_values_and_indices(num_list: list):
    total = 0
    for index, num in enumerate(num_list):
        total += (num + index)
        
    return total

print(sum_of_values_and_indices([]))
print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0]))

strings = ["enchanted", "sparks fly", "long live"]

def in_list(strings: list, string: str):
    for index, text in enumerate(strings):
        if (text == string):
            return index
    return -1

print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen"))  
print(in_list(strings, "love story"))

def sum_from(num1: int, num2: int):
    summ = 0
    for num in range(num1, (num2 + 1)):
        summ += num
    
    return summ

print(sum_from(5, 12))

def same_index_values(list1: list, list2: list):
    new_list = []
    for index, elements in enumerate(list1):
        if (elements == list2[index]):
            new_list.append(index)
    
    return new_list

print(same_index_values([3,2,2,1], [1,2,2,3]))