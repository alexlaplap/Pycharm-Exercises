# Calling Function
from utils import find_max
# Input Data
try:
    print('Largest number Game')
    a = int(input('Type 1st Number: '))
    b = int(input('Type 1st Number: '))
    c = int(input('Type 3st Number: '))
    d = int(input('Type 4st Number: '))
    e = int(input('Type 5st Number: '))
    # Defining List
    elements = [a, b, c, d, e]
    # Calling Module
    high = find_max(elements)
    print(f'The highest number is {high}.')
except ValueError:
    print('The Data input must be a number.')