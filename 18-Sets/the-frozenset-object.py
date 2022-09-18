#the frozenset function creates an IMMUTABLE set from an iterable object such as a list/tuple
# since a frozenset is IMMUTABLE, it can serve as a KEY in a DICTIONARY
freeze = frozenset([1, 2, 3, 2])
print(freeze)
print(dir(freeze))

print()

print({freeze : "Values"})