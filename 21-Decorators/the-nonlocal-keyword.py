# the non-local keyword is complementary to the global keyword 
# but in this case it is used in a nested function, in
# order to reference the variable in the enclosing function 
# and not create a variable local to the nested function

def outer():
    bubble_tea_flavor = "Black"
    def inner():
        nonlocal bubble_tea_flavor
        bubble_tea_flavor = "Taro"
    inner()
    return bubble_tea_flavor

print(outer())