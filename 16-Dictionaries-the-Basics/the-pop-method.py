release_dates = {
    "Python": 1991,
    "Java": 1995,
    "Ruby": 1995,
    "Go": 2007
}

#the pop method returns the value deleted of the keyword
print(release_dates.pop("Go"))
print(release_dates)

if "C++" in release_dates:
    release_dates.pop("C++")

#the second argument provides a default value the program will return 
#if the key does not exist
#if the key exists, it will return it original value
print(release_dates.pop("C++", 2000))
print(release_dates.pop("Ruby", 2000))

release_dates = {
    "Python": 1991,
    "Java": 1995,
    "Ruby": 1995,
    "Go": 2007
}

#the del method does the same thing 
#expect it does not return the value of the deleted keyword 
#and it doesn't accept the second parameter

del release_dates["Ruby"]
print(release_dates)
