index = [
    [1,2,3],
    [4,8,12],
    [13,26,39]
]
index[1][1] = 100
print(index[2][2])
print(index[0][0])
print(index[1][1])

for x in index:
    for y in x:
        print(y)