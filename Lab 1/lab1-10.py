def word_count(text):
    list = text.split()
    count = len(list)
    print(f"Textul dat are {count} cuvinte.")

text = input("Introduceti textul: ")
word_count(text)
