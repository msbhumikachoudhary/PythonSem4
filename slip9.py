# QUESTION 1
# Write a Python program to create a tuple using two different tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print("New Tuple : ",new_tuple)


# QUESTION 2
# Write a Python program to sort (ascending and descending) a dictionary by value
my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 1}
# Sort dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# Sort dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("SORTED IN ASCENDING ORDER : " ,sorted_dict_asc)
print("SORTED IN DESCENDIG ORDER : ", sorted_dict_desc)