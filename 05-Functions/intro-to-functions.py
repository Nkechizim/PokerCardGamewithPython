def output_text():
    print("Hey!")

output_text()

#python doesn't actually check the datatype of argument, it's just for documentation
#so if you pass in another datatype it doesn't throw an error
def p(text: str):
    print(text)

p("Hello Mamacita")

#assigning default arguments to a function 
def add(a:int = 0, b:int = 0, c:int = 0) -> int:
    sum = a + b + c
    return(sum)

#Postional and Keyword Arguments
result = add(5, b = 67, c = 54)
print("The total is", result)
result = add(5, 98, c = 54)
print("The total is", result)
result = add(5, 98, 54)
print("The total is", result)

#fallling back on default arguments when one or more arguments are missing
print(add())
print(add(10))
print(add(10, 15))
print(add(10, c = 15))

def convert_to_currency(amount:int):
    print("$"+str(amount))

convert_to_currency(15)