#the function without any input creates an empty set, 
print(set())
#an empty curly braces creates an empty dictionary not an empty set
{}
#with inputs provided, it tries to convert the input to a set,
#the input must be an iterable object
print(set([1,2,3]))
print(set([1, 2, 3, 3, 2, 1]))

print(set((1, 2)))
print(set((1, 2, 3, 1)))

print(set("abc"))
print(set("aabbcc"))

print(set({"key": "value"}))

philosophers = ["plato", "socrates", "pythagoras", "plato", "aristotle", "pythagoras"]

philosophers = list(set(philosophers))
print(philosophers)