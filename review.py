def remove_uppercase(input_string):
    return ' '.join(char.lower() for char in input_string if not char.isupper())
    
def FizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
def gcd(larger, smaller):
    while larger > smaller:
        if larger != 0 and smaller != 0:
            larger = larger - smaller
        else:
            smaller = smaller / larger
    if smaller == 0:
        print("Answer: ")
        return larger
    else:
        print("Answer: ")
        return smaller
def factorial(n):
    return 1 if (n==1 or n == 0) else n * factorial(n - 1)



    
input_string = "Hello World"
n = 5
number = 120
larger = int(input("Enter the larger number: "))
smaller = int(input("Enter the smaller number: "))


result = remove_uppercase(input_string)
fizzled = FizzBuzz(number)
print(factorial(n))
print(result)
print(fizzled)
print(gcd(larger, smaller))
