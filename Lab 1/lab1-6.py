def palindrom(num):
    copy = num
    copy = copy[::-1]
    if(copy == num):
       print("Numarul este palindrom.")
    else: print("Numarul nu este palindrom")

num = input("Introduceti numarul: ")
palindrom(num)