text = input("Introduceti textul UpperCamelCase: ")
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = [text[0].lower()]

for i in text[1:]:
    if i in upperCase:
        result.append('_')
        result.append(i.lower())
    else: result.append(i)

print("".join(result))