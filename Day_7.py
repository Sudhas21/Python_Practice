#Count number of vowels in a given string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))

# check whether the given num is prime


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")


#Calculate factorial of a given number
    
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

