import random

# For generating any number:
print(random.random())

# Example No.01:
for x in range(10):
    print(random.random())

# Example No. 02:
# For generating any number but within specific range:
for x in range(3):
    print(random.randint(10, 20))


# For generating any string based from a certain list:
members = ['Alex', 'Bason', 'Wil', 'Arvin', 'Robert', 'Bronia', 'Quinto',
            'Cocoy', 'Mikko']
print(f'Treat will be paid by: {random.choice(members)}.')