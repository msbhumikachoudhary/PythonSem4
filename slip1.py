#QUESTION 1
#  Write a Python function to check whether a number is in a given range. 
def is_in_range(number, start, end):
    return start <= number <= end

number = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if is_in_range(number, start, end):
    print(f"The number {number} is within the range [{start}, {end}].")
else:
    print(f"The number {number} is not within the range [{start}, {end}].")




#QUESTION 2
# Write a Python program to find set difference, union, intersection and symmetric difference.
set1 = set(input("Enter elements for set 1 (space-separated): ").split())
set2 = set(input("Enter elements for set 2 (space-separated): ").split())
difference = set1 - set2
print("Set difference (set1 - set2):", difference)
union = set1 | set2
print("Set union (set1 | set2):", union)
intersection = set1 & set2
print("Set intersection (set1 & set2):", intersection)
symmetric_difference = set1 ^ set2
print("Set symmetric difference (set1 ^ set2):", symmetric_difference)