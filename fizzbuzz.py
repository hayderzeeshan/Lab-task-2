import random

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzBuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
    
start = 1
end = 100

for num in range(10):
    num = random.randint(start , end)
    result = fizz_buzz(num)
    print(f"Number:{num},Result:{result}")
