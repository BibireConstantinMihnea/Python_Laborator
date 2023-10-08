def extract_number(text):
    empty_string = ""

    for i in text:
        if i.isdigit():
            empty_string = empty_string + i
        elif i.isascii() and empty_string != "":
            break
    print(f"Numarul din text este: {empty_string}")

text = input("Introduceti textul: ")
extract_number(text)
