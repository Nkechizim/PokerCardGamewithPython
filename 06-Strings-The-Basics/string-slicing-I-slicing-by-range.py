def slicing(text1: str):
    
    #slicing a string into half using range(even number)
    if(len(text1) % 2 == 0):
        a = int(len(text1) / 2)
        print(text1[ : a] + "...", end="")
        print(text1[a : ] + " ")
        #printing out the entire string but in steps of 2
        print(text1[ : : 2] + " ")
    #slicing a string into half using range(odd number)
    else:
        a = int((len(text1) / 2) + 0.5)
        print(text1[ : a] + "...", end="")
        print(text1[a : ])
        #printing out the entire string but in steps of 3 from the back
        print(text1[ : : -3] + " ")
        #printing out the entire string but in steps of 1 from the back
        #so we are just basically reversing the string
        print(text1[ : : -1] + " ")

slicing("Nkechukwuyem Deborah Chizim")

#check if a string backwards is exactly the same as it is forward
def is_palindrome(text: str):
    return text[::-1] == text

print(is_palindrome("nky"))