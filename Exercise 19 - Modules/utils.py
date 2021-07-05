def find_max(elements):
    # Redefining 'list' thru new variable
    numbers = elements
    # Set highest number based from 1st element in list.
    high = numbers[0]
    # Working Equation
    for x in numbers:
        if x > high:
            high = x
    # Value Returned to main.py
    return high