def bit_count(num):
    copy_num = num
    count = 0

    while copy_num:
        count += copy_num & 1
        copy_num >>= 1

    print (f"Numarul {num} are {count} biti cu valoarea 1 in reprezentarea binara.")

num = int(input("Introduceti un numar: "))
bit_count(num)
