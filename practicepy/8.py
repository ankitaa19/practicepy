def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number to check for primality: "))
if is_prime(number):
    print("It's a prime number!")
else:
    print("It's not a prime number.")