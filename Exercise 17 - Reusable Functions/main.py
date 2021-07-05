def emoji(message):
    words = message.split(' ')
    emoticons = {
        ":)": "😊",
        ":(": "😢",
    }
    output = ""
    for y in words:
        output += emoticons.get(y, y) + " "
    return output


message = input('Your Message: ')
emoji(message)
print(emoji(message))