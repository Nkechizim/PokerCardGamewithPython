import functools

def be_nice(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("Hey There!! Let's start decorating")
        result = func(*args, **kwargs)
        print("It was lovely decorating you")
        return result
    
    return inner

@be_nice
def func_to_be_decorated(a, b):
    "Adds two numbers together" #this is called a docstring, describes the function
    return a + b

#print(func_to_be_decorated(3, 5))

#when a function is decorated, the documentation is lost, 
#as we are actually calling the 'inner' function, which then calls the original function

#the functools helps to preserve the original documentation
help(func_to_be_decorated)

