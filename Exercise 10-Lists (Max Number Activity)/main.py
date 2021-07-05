print('Largest number Game')
a = int(input('Type 1st Number: '))
b = int(input('Type 2st Number: '))
c = int(input('Type 3st Number: '))
d = int(input('Type 4st Number: '))
e = int(input('Type 5st Number: '))
list = [a,b,c,d,e]
y = 0
for x in list:
      if x > y:
         y = x
      else:
          x = y
print(f'You have the following numbers {list} in this list.')
print(f'The highest number is {y}.')
