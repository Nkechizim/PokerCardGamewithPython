def in_and_not_in(text1: str, text2: str):
    
    #checking if a string exists in another string or not
    if(text1 in text2):
        position = text2.find(text1) #find the beginning position of text1 in text2
        print("Yaay!!,", text1,"is in",text2,"beginning at position", position)
    if(text1 not in text2):
        print("Sorry,", text1,"is not in",text2)
    
    if(text2 in text1):
        position = text1.find(text2) #find the beginning position of text2 in text1
        print("\nBut,", text2,"is in",text1,"beginning at position", position)
    if(text2 not in text1):
        print("\nBut,", text2,"is not in",text1,"!!")

in_and_not_in("Nkechukwuyem Deborah Chizim", "Chizim")