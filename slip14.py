# QUESTION 1
# Write a Python program to create a tuple of n numbers and print maximum, minimum, and sum of elements in a tuple
n = int(input("Enter the number of elements: "))
# Create a tuple of n numbers
numbers = tuple(int(input("Enter a number: ")) for _ in range(n))
# Print the maximum, minimum, and sum of elements in the tuple
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# QUESTION 2
# Write a Python program which accept an integer value ‘n’ and display all prime numbers till ‘n’.
def is_prime(num):
    if num < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If the number is divisible by any number between 2 and its square root, it's not prime
            return False
    return True
n = int(input("Enter a number: "))
# Display all prime numbers up to n
prime_numbers = [num for num in range(2, n+1) if is_prime(num)]
print("Prime numbers up to", n, "are:", prime_numbers)
