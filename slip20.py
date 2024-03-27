# QUESTION 1
# Write an anonymous function to calculate area of square.
calculate_area = lambda side: side ** 2
side = int(input('Enter the side of square : '))
area = calculate_area(side)
print(f"AREA OF SQUARE WITH SIDE {side} is : ",area)


# QUESTION 2
# Write a Python program which finds sum of digits of a number.
# Example n=130 then output is 4 (1+3+0).
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