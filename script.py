from simple_functions import double_number, square_number

"""
Define a variable 'a' and assign it the value 5
Print the value of 'a' before doubling
"""
a = 5
print(f'value before double_number(): {a}')

"""
Double the value of 'a' using the 'double_number' function
Print the value of 'a' after doubling
"""
result = double_number(a)
print(f'value after double_number(): {result}')

"""
Print the value of 'a' before squaring
"""
print(f'value before square_number(): {a}')

"""
Square the value of 'a' using the 'square_number' function
Print the value of 'a' after squaring
"""
result = square_number(a)
print(f'value after square_number(): {result}')
