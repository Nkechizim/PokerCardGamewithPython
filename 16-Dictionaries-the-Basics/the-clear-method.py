release_dates = {
    "Python": 1991,
    "Java": 1995,
    "Ruby": 1995,
    "Go": 2007
}

#del release_dates


#the clear method deletes all key value pairs within the dictionary 
#but leaves the variable name with an empty dictionary
release_dates.clear()
print(release_dates)

#the delete keyword (without square brackets) 
#deletes an entire variable with all its content from memory
del release_dates
#print(release_dates)