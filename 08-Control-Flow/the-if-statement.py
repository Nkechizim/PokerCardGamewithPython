def truthy_or_falsy(argu):
    if(argu):
        return "The value "+ str(argu) + " is truthy"
    if(not argu):
        return "The value " + str(argu) + " is falsy"

print(truthy_or_falsy(0))

print(0 - (-5))