def first_longer_than_second(text1: str, text2: str):
    #printing each character in a string starting from the beginning 0
    x=0
    while(x < len(text1)):
        print(text1[x] + " ", end="")
        x+=1

    print("\n")
    #printing each character in a string starting from the end
    x = len(text1) -1 
    while(x >= 0):
        print(text1[x] + " ", end="")
        x-=1
    
    print("\n")
    for y in text2:
        print(y, end= " ")
    
    print("\n")
    #printing each character in a string starting from the end 
    #(-1 represents the last character in a string)
    y=1
    while(y <= len(text2)):
        print(text2[-y] + " ", end="")
        y+=1

    #checking if the length of string 1 is greater than that of string 2
    print("\n")
    if (len(text1) > len(text2)):
        return True
    else:
        return False

print(first_longer_than_second("word", "Dictionary"))

def same_first_and_last_letter(text: str = " "):
    return True if(text[0] == text[-1]) else False

print(same_first_and_last_letter("Runner"))