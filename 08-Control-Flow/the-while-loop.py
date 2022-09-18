invalid_number = True

while invalid_number:
    user_value = int(input("Please enter a number greater than 10: "))
    if(user_value > 10):
        print("Perfect! Great Choice")
        invalid_number = False
    else:
        print(f"Sorry {user_value} is not greater than 10")

def fizzbuzz(num: int = 0):
    count = 0
    while (count <= num):
        
        if(count % 3 == 0 and count % 5 != 0):
            print("Fizz")
        elif(count % 5 == 0 and count % 3 != 0):
            print("Buzz")
        elif(count % 3 == 0 and count % 5 == 0):
            print("FizzBuzz")
        else:
            print(count)
        count += 1

fizzbuzz(16)