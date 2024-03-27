# QUESTION 1
# Write a program which prints Fibonacci series of a number. 
nterms = int(input ("How many terms the user wants to print? "))  
n1 = 0  
n2 = 1  
count = 0  
if nterms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
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


# QUESTION 2
# Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary (n = 5)
# Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
n = int(input("Enter a number: "))
# Generate the dictionary using a dictionary comprehension
result_dict = {x: x*x for x in range(1, n+1)}
# Print the dictionary
print(result_dict)
