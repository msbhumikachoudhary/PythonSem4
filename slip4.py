# QUESTION 1
# Write a Python program to find the repeated items of a tuple
tuple_data = (1, 2, 3, 2, 4, 1, 5, 2)
repeated_items = []
for item in tuple_data:
    if tuple_data.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print("Repeated items in the tuple:", repeated_items)



# QUESTION 2
# Write a Python program to create a set with any 3 weekdays. Add single element to the set and print it. Add multiple elements and print the set.
weekdays = {"Monday", "Tuesday", "Wednesday"}
print("Original Set : ", weekdays)
# Add a single element to the set
weekdays.add("Thursday")
print("Set after adding a single element:", weekdays)
# Add multiple elements to the set
new_weekdays = {"Friday", "Saturday", "Sunday"}
weekdays.update(new_weekdays)
print("Set after adding multiple elements:", weekdays)
