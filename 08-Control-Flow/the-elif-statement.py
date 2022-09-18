def calculator(operation: str = "add", a: int = 0, b: int = 0):
    if(operation == "add" or operation == "Add"):
        result = a + b
        return result
    elif(operation == "subtract" or operation == "Subtract"):
        result = a - b
    elif(operation == "multiply" or operation == "Multiply"):
        result = a * b
    elif(operation == "divide" or operation == "Divide"):
        result = a / b
    else:
        result = "I don't understand what operation you want me to do!"
    
    return result

print(calculator("Add", 7, 6))
print(calculator("add", 7, 6))
print(calculator("Subtract", 7, 6))
print(calculator("subtract", 7, 6))
print(calculator("Multiply", 7, 6))
print(calculator("multiply", 7, 6))
print(calculator("Divide", 7, 6))
print(calculator("divide", 7, 6))
print(calculator("division", 7, 6))
