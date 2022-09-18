#the LEGB Rule means: "Local/ Enclosing Functions/ Global/ Built-in 
# (pyhton's built-in keywords)"

x = 25

#the local scope wins out
def outer():
    x = 10
    def inner():
        x = 5
        return x

    return inner()

print(outer())

#the enclosing function scope wins out
def outer():
    x = 10
    def inner():
        return x

    return inner()

print(outer())

#the global scope wins out
def outer():
    def inner():
        return x
    
    return inner()

print(outer())

#the built-in keyword scope wins out
def outer():
    def inner():
        return len
    
    return inner()

print(outer()("Python"))