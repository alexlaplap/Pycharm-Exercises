print('Duplicate Number Remover')
a = (input('Type 1st Number: ')).upper()
b = (input('Type 2nd Number: ')).upper()
c = (input('Type 3rd Number: ')).upper()
d = (input('Type 4th Number: ')).upper()
e = (input('Type 5th Number: ')).upper()
list = [a,b,c,d,e]
list2 = []
for x in list:
    if x not in list2:
        list2.append(x)
print(list2)