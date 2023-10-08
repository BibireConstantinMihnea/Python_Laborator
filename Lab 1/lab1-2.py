text = input("Introduceti o propozitie: ")
count = 0
vowels = "aeiouAEIOU"
for i in text:
    if (i in vowels):
        count = count + 1

print(f"Propozitia {text} contine {count} vocale.")