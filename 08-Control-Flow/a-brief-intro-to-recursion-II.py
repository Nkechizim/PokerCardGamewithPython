def reverse_string(text: str):

    if(len(text) - 1 >= 0):
        print(text[-1], end="")
        reverse_string(text[ : -1])
    else:
        return
    
reverse_string("chizim")

print()

def factorial(num: int):
    if num > 1:
       return num * factorial(num-1)
    else:
        return num 

    
print(factorial(5))
print(factorial(4))
print(factorial(6))