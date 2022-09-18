def count_down_from(num: int):
    while(num >= 0):
        print(num)
        num -= 1

count_down_from(5)

print()

def count_down_from(num: int):
    if num < 0:
        print(num)
        count_down_from(num + 1)
    elif num == 0:
        print (num)
        return
    else:
        print(num)
        count_down_from(num - 1)

count_down_from(-8)

print()

count_down_from(6)