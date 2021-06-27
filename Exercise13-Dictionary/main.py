number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
input = input('10-Digit Phone Number:')
final = ""
for x in input:
    final += number.get(x) + " "
print(final)