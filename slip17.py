# QUESTION 1
# Write a Python program to accept and convert string in uppercase or vice versa. 
string = input("Enter a string: ")
if string.isupper():
    converted_string = string.lower()
elif string.islower():
    converted_string = string.upper()
else:
    converted_string = string
print("Converted string:", converted_string)



# QUESTION 2
# Write a Python program which accepts an integer value ‘n’ and display all prime numbers till ‘n’.
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



#QUESTION 3
n = 3
num = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end="   ")
        num += 1
    print()
