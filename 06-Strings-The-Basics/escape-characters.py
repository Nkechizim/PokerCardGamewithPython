print("This is \nNkechi Chizim")
print("\tOnce upon a time")
#using a blackslash in front of a quote 
#within a string to stop python from interpreting 
#it as the start or end of the string
print("\"Let Love Win\", Nkechi")
print('\'Let Love Win\', Nkechi')
print("Let's print a blackslash \\")
print("Let's print a blackslash \ ")

# use r(raw string) to avoid python interpreting normal text as special characters
print(r"C:\news\travel")

some_random_number = 5
another_very_random_number = 67
a_third_very_random_number = 85
the_last_randon_number =96

#use a blackslash to spread a long line of code over multiple lines 
#without having errors
final = some_random_number + \
        another_very_random_number + \
        a_third_very_random_number +  \
        the_last_randon_number

print(final)