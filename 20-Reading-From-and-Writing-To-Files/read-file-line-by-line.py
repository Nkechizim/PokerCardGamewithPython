with open("cupcakes.txt") as file_object:
    for line in file_object:
        print(line)

with open("cupcakes.txt") as file_object:
    for line in file_object:
        print(line.rstrip())

#with open("cupcakes.txt") as file_object:
#    for line in file_object:
#        print(line.strip())