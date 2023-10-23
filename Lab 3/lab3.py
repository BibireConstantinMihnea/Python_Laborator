#1.
# def fibonacci(n): 
#     if n == 0: 
#         return 0
#     elif n == 1: 
#         return 1
#     else: 
#         return fibonacci(n-2)+fibonacci(n-1) 

# def fibo_n(n):
#     fibo = []
#     for i in range(0, n):
#         fibo.append(fibonacci(i))
#     return fibo

# n = 5
# print(fibo_n(n))
#----------------------------------------------------
#2.
# import math
 
# def is_prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True

# def prime(lista):
#     prime_nums = []
#     for i in lista:
#         if(is_prime(i) == True):
#            prime_nums.append(i)
#     return prime_nums

# lista = [1, 2, 3, 4, 5, 6, 7]
# print(prime(lista))
#----------------------------------------------------
#3.
# def list_op(lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     union = list(set1.union(set2))
#     intersection = list(set1.intersection(set2))
#     a_dif_b = list(set1.difference(set2))
#     b_dif_a = list(set2.difference(set1))
#     print(f"Reuniunea = {union}\nIntersectia = {intersection}\nA - B = {a_dif_b}\nB - A = {b_dif_a}")

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 1]
# list_op(lista1, lista2)
#----------------------------------------------------
#4.
# def song(notes, moves, start):
#     song = []
#     song.append(notes[start])
#     index = start
#     for move in moves:
#         if(index + move > len(notes)):
#             index = -1
#             index = index + move
#         else: index = index + move
#         song.append(notes[index])
#     print(song)

# notes = ["do", "re", "mi", "fa", "sol"]
# moves = [1, -3, 4, 2]
# start = 2
# song(notes, moves, start)
#----------------------------------------------------
#5.
# def diag(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if i > j:
#                 matrix[i][j] = 0
#     return matrix

# matrix = [[1, 2, 3], 
#           [4, 5, 6], 
#           [7, 8, 9]]
# print(diag(matrix))
#----------------------------------------------------
#6.
# def x_appearances(lists, x):
#     dictionary = {}
#     result = []
#     for i in range(len(lists)):
#         for j in range(len(lists[0])):
#             if(dictionary.get(lists[i][j]) == None):
#                 dictionary.setdefault(lists[i][j], 1)
#             else: dictionary.update({lists[i][j]: dictionary.get(lists[i][j]) + 1})
#     for i in dictionary.keys():
#         if(dictionary.get(i) == x):
#             result.append(i)
#     return result

# lists = [[1,2,3], [2,3,4], [4,5,6], [4,1, "test"]]
# x = 2
# print(x_appearances(lists, x))
#----------------------------------------------------
#7.
# def palindrom(num):
#     str_num = str(num)
#     copy = str_num
#     copy = copy[::-1]
#     if(copy == str_num):
#        return True
#     else: return False

# def tuple_palindrome(list):
#     count_pal = 0
#     greatest_pal = 0
#     for i in list:
#         if palindrom(i) == True:
#             count_pal += 1
#             if(i > greatest_pal):
#                 greatest_pal = i
#     return (count_pal, greatest_pal)

# List = [1, 212, 12321, 122, 11, 25, 0]
# print(tuple_palindrome(List))
#----------------------------------------------------
#8.
# def ascii_div(x, list, flag):
#     final_list = []
#     for i in list:
#         string_list = []
#         for ch in i:
#             if flag == True:
#                 if ord(ch) % x == 0:
#                     string_list.append(ch)
#             elif flag == False:
#                 if ord(ch) % x != 0:
#                     string_list.append(ch)
#         final_list.append(string_list)
#     return final_list

# x = 2
# List =  ["test", "hello", "lab002"]
# flag = False
# print(ascii_div(x,List,flag))
#----------------------------------------------------
#9.
# def bad_seat(matrix):
#     bad_seat = []
#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             current_height = matrix[row][col]

#             for i in range(row + 1, len(matrix)):
#                 if matrix[i][col] <= current_height:
#                     bad_seat.append((i,col))
#     return list(set(bad_seat))

# matrix = [[1, 2, 3, 2, 1, 1],
#           [2, 4, 4, 3, 7, 2],
#           [5, 5, 2, 5, 6, 4],
#           [6, 6, 7, 6, 7, 5]] 
# print(bad_seat(matrix))
#----------------------------------------------------
#10.
# def first_element(lists):
#     new_list = [[0 for rows in range(len(lists))] for cols in range(len(lists[0]))]
#     final_list = []
#     for row in range(len(lists)):
#         for col in range(len(lists[0])):
#             new_list[col][row] = lists[row][col]
#     for tup in new_list:
#         final_list.append(tuple(tup))
#     return final_list

# lists = [[1,2,3], [5,6,7], ["a", "b", "c"]]
# print(first_element(lists))
#-------------------------------------------------------
#11.
# def custom_sort(tup):
#     return tup[1][2]
# def order(List):
#     List.sort(key = custom_sort)
#     return List
# List = [('abc', 'bcd'), ('abc', 'zza')]
# print(order(List))
#-------------------------------------------------------
#12.
def group_by_rhyme(word_list):
    rhymes = {}
    for word in word_list:
        rhyme = word[-2:]
        if rhyme in rhymes:
            rhymes[rhyme].append(word)
        else: rhymes[rhyme] = [word]
    return list(rhymes.values())
word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
print(group_by_rhyme(word_list))