#cupcakes_file.close() this method does not close 
#the file if an error occurs before reaching it

#this closes the file as soon as the block of code is done running, 
#even if there's an error

#with open("cupcakes.txt", "r") as cupcakes_file:
#    print("The file has been opened")
#    content = cupcakes_file.read()
#    print(content)
#print("The file has been closed")

filename = input("Choose a file to open: ")

with open(filename, "r") as file_object:
    print(file_object.read())