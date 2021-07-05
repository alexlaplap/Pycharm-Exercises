a = input('Please enter name: ')
b = len(a)
if b < 3:
    print('Name must be 3 characters long.')
elif b > 50:
    print('Name must not exceed 50 characters long.')
else:
    print('Name is registered.')