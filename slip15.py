# QUESTION 1
# Write a python program to check if a string is a Palindrome or not.
def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")



# QUESTION 2
# Write a Python program which finds sum of digits of a number. [20 M]
# Example n=135 then output is 9 (1+3+5).
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        sum_digits += digit  # Add the digit to the sum
        number //= 10  # Remove the last digit
    return sum_digits

input_number = int(input("Enter a number: "))
digit_sum = sum_of_digits(input_number)
print("Sum of digits:", digit_sum)