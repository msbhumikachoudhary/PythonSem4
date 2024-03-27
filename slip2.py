# QUESTION 1
# Write a Python program to get the 4th element from front and 4th element from last of a tuple
tuple_data = (33, 66, 99, 11, 22, 44, 88, 112)

if len(tuple_data) >= 4:
    fourth_from_front = tuple_data[3]
    fourth_from_end = tuple_data[-4]
    print("Fourth element from the front:", fourth_from_front)
    print("Fourth element from the end:", fourth_from_end)
else:
    print("The tuple does not have enough elements.")



#QUESTION 2
# Write a Python program to perform given operations on set. [20 M]
# a. check whether 2 sets are equal or not
# b. Symmetric difference
# c. Intersection of sets
# d. Find maximum and the minimum value in a set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

are_equal = set1 == set2
print("Set Equality : ", are_equal)

symmetric_difference = set1 ^ set2
print("Symmetric difference:", symmetric_difference)

intersection = set1 & set2
print("Intersection of sets:", intersection)

max_value = max(set1)
min_value = min(set1)
print("Maximum value in the set:", max_value)
print("Minimum value in the set:", min_value)
