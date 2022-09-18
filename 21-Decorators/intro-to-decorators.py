#Decorator Functions are functions that both accepts a function 
# as an argument and returns a function as a return value

def be_nice(func):
    def inner():
        print("Hey There!! Let's start decorating")
        func()
        print("It was lovely decorating you")
    
    return inner

def func_to_be_decorated():
    print("Thanks for decorating decorate me!!")

be_nice(func_to_be_decorated)()

print()
#syntaxtic sugar is a syntax that makes things
# easier to read or understand in a language
# with this syntax, the declared function is directly passed on to be_nice 
# and we can call the function on its own
@be_nice
def func_to_be_decorated():
    print("Thanks for decorating decorate me!!")

func_to_be_decorated()

import functools

print()

def uppercase(fn):

    @functools.wraps(fn)

    def wrapper(*args, **kwargs):

        return fn(*args, **kwargs).upper()



    return wrapper



@uppercase

def concatenate(a, b):

    """Combines two strings together"""

    return a + b



print(concatenate("pyt", "hon"))