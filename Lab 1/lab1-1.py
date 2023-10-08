def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

a = int(input("Introduceti primul numar: "))
b = int(input("Introduceti al doilea numar: "))
result = gcd(a,b)
print(f"Cel mai mare divizor comun al lui {a} si {b} este {result}")