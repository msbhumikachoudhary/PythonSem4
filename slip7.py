# QUESTION 1
# Write a Python program to find maximum and the minimum value in a set. 
set1 = (45, 67, 91, 55, 72, 84, 100, 999)
maxv = max(set1)
minv = min(set1)
print("Maximum Value from set : ", maxv)
print("Minimum Value from set : ", minv)



# QUESTION 2
# Write a Python program to unpack a tuple in several variables. Display type of each variable.
my_tuple = (1, 'hello', 3.14)
var1, var2, var3 = my_tuple
print("Variable 1:", var1, "- Type:", type(var1))
print("Variable 2:", var2, "- Type:", type(var2))
print("Variable 3:", var3, "- Type:", type(var3))