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
def diag(matrix):
    new_mat = []
    for i in range(1,len(matrix)):
        for j in range(i):
            
    return new_mat

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(diag(matrix))