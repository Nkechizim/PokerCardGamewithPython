def be_nice(func):
    def inner(*args, **kwargs):
        print("Hey There!! Let's start decorating")
        result = func(*args, **kwargs)
        print("It was lovely decorating you")
        return result
    
    return inner

@be_nice
def func_to_be_decorated(a, b):
    return a + b

print(func_to_be_decorated(3, 5))