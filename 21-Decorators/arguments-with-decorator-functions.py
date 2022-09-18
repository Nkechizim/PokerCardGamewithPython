def be_nice(func):
    def inner(*args, **kwargs):
        print("Hey There!! Let's start decorating")
        func(*args, **kwargs)
        print("It was lovely decorating you")
    
    return inner

@be_nice
def func_to_be_decorated(decorator, position):
    print(f"Thanks for decorating decorate me {position } {decorator}!!")

# by passing the argument needed for the func_to_be_decorated as on line 16, 
# we are actually passing it to the nested inner function on line 2

func_to_be_decorated("Nkechi", position = "CEO")

