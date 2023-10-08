def most_common_letter(str):
    new_str = str.lower()
    map = {}
    for char in new_str:
        if char.isalpha():
            if char in map:
               map.update({char: map.get(char) + 1})
            else: 
               map.setdefault(char, 1)

    highest_count = 0
    for char in map:
        if map.get(char) > highest_count:
            highest_count = map.get(char)
            letter = char
    
    print(f"Cea mai comuna litera este {letter} cu {highest_count} aparitii.")

text = input("Introduceti textul: ")
most_common_letter(text)