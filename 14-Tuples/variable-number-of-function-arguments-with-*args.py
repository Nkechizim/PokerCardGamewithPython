#the variable name args is just very popular but it can be anything
def accept_stuff(*args):
    print(type(args))
    print(args)

accept_stuff()
accept_stuff(1)
accept_stuff(1, 2)
accept_stuff(1, 89, 3)
accept_stuff(1, "boy", 3, 4)


def maximum(*numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num

print(maximum(23, 76, 8, 456, 98))
print(maximum(23, 76, 8, 456, 98, 0, 56))
print(maximum(23, 76, 8, 48, 98, 0, 56, 46))
print(maximum())

print()

#in this case, the first argument passed in is used as the first parameter, 
#while the others are used to form a tuple
def maximum(nonsense, *numbers):
    print(nonsense)
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num

print(maximum(789, 23, 76, 8, 456, 98))
print(maximum(1238, 23, 76, 8, 456, 98, 0, 56))
print(maximum(1, 23, 76, 8, 48, 98, 0, 56, 46))
print(maximum("horray"))

print()

#in this case you have to explicit define the other arguments, 
#if not every parametes passed in would be used to form a tuple
def maximum(*numbers, nonsense):
    print(nonsense)
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num

print(maximum(789, 23, 76, 8, 456, nonsense = 98))
print(maximum(1238, 23, 76, 8, 456, 98, 0, nonsense = 56))
