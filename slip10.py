# QUESTION 1
# Write an anonymous function to calculate area of square
calculate_area = lambda side: side ** 2

side = int(input('Enter the side of square : '))
area = calculate_area(side)
print(f"AREA OF SQUARE WITH SIDE {side} is : ",area)


# QUESTION 2
# Write a Python program to count frequency of each character in a given string using user defined function
string = input('Enter any string : ')
char_counts = {}
for char in string:
    char_counts[char] = char_counts.get(char, 0) + 1
print("CHARACTER COUNT IN THE STRING : ", char_counts)
