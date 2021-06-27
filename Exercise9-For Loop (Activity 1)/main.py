x = int(input('Price#1 in $: ').upper())
y = int(input('Price#2 in $: ').upper())
z = int(input('Price#3 in $: ').upper())
total = 0
for price in (x,y,z):
    total = total + price
print(f'Total: ${total}')
