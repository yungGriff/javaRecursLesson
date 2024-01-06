#This algorithm calculates the greatest common divisor (GCD) of two positive integers, m and n, using the Euclidean algorithm.

print("Find the GCD between two numbers.")
def gcd(larger, smaller):
    while larger != 0 and smaller != 0:
        if larger > smaller:
            larger = larger - smaller
        else:
            smaller = smaller - larger
    if smaller == 0:
        print("answer: ")
        return larger
    else:
        print("answer: ")
        return smaller


# Get the values from the user
while True:
    larger = int(input("Enter the larger number: "))
    smaller = int(input("Enter the smaller number: "))
    if larger == 0 or smaller == 0:
        print("Both numbers must be non-zero. Please enter new values.")
        continue
    else:
        break
print(gcd(larger, smaller))
