# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# sample input: 10

# sample output: 35

adding = lambda x : x + 25

x = eval(input("Sample input: "))

print("Sample output", adding(x))
_______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]


list1 = list(map(eval, input("Enter Sample List: ").split()))
new = lambda x : x*3
new_list = list(map(new, list1))

print(new_list)
________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

list1 = list(map(int, input("Enter Sample List: ").split()))

squre = lambda x : x**2

squre_list = list(map(squre, list1))
print("Squre the element of the list: ", squre_list)
