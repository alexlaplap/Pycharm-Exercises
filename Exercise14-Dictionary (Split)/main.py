mensahe = input('Your Message: ')
kotobas = mensahe.split(' ')
emotions = {
    ":)":"😊",
    ":(":"😢",
}
output = ""
for y in kotobas:
    output += emotions.get(y,y) + " "
print(output)