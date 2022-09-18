def delete_all(strings, target):
    while target in strings:
        strings.remove(target)
    return strings

print(delete_all([4, 4, 4, 4], 4))
print(delete_all([5, 3, 5, 5, 6], 5))