a = input('What is your weight? ')
b = input("Press 'L' for lbs (pounds) or 'K' for kgs (kilograms) with respect to the unit of your inputted weight: ")
if b == 'l' or b == 'L':
    c = float(a) / 2.2
    print(f'You are {c} kgs.')
elif b == 'k' or b == 'K':
    c = float(a) * 2.2
    print(f'You are {c} lbs.')
else:
    print('Wrong input.')