#Write a Python program to square the elements of a list using map() function.
numbers = list(map(int, input('Enter numbers in a list:')))

square_numbers = list(map(lambda x: x**2, numbers))

print(square_numbers)