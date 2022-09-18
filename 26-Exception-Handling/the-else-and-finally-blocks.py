# x = 10

try:
    print(x + 5)
except NameError:
    print("Some variable does not exist")
else:
    print("This will only print if there is no error in the try")
finally:
    print("This will print with or without error!")
    print("Closing the file!!")