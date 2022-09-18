def add(a, b):
    assert isinstance(a, int) and isinstance(b, int), "Both arguments must be integers"
    return a + b

print(add(7, 9))
print(add(7, "9"))