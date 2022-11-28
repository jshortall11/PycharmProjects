for number in range(0, 101, 1):
    print(f"Next number is: {number}")
    if number in range (3,101,3):
        print("Fizz")
    if number in range (5,101,5):
        print("Buzz")
    if number in range (3 and 5 , 101, 3 and 5):
        print("FizzBuzz")

