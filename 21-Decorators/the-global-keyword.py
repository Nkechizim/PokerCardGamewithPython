# the Global keyword allows you to create or modify 
# a global variable within a local scope

x = 10

def something():
    global x
    x = 15

print(x)
something()
print(x)

