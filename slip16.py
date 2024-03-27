# QUESTION 1
# Write a Python program to create tuple of n numbers, print the first half values of tuple in one line and the last half values of tuple on next line.
def print_tuple_halves(n):
    numbers = tuple(range(1, n+1))
    half = len(numbers) // 2
    first_half = numbers[:half]
    last_half = numbers[half:]
    print(*first_half)
    print(*last_half)
n = 14
print_tuple_halves(n)


# QUESTION 2
# Write a Python program which prints fibonacci series of a number
nterms = int(input ("Enter the 'n'th term : "))  
n1 = 0  
n2 = 1  
count = 0  
if nterms <= 0:  
    print ("Please enter a positive integer !!")  
elif nterms == 1:  
    print ("The Fibonacci sequence of the numbers up to", nterms, ": ")  
    print(n1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < nterms:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count += 1 