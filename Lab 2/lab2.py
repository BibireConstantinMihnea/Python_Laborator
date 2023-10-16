# 0.
# n = int(input("Introduceti n: "))
# sum = 0
# for i in range(n+1):
#     sum = sum + i

# print (sum)

#------------------------------------------------
# 1.
# input = [n for n in range(ord('A'), ord('A') + 26)]
# result = " ".join(hex(n)[2:] for n in range(ord('A'), ord('A') + 26))

# print(result)

#---------------------------------------------------
# 2.
# c = " ".join(bin(n)[2:].rjust(8, '0') for n in range(5))
# count_0 = c.count('0')
# count_1 = c.count('1')
# print(c, count_0, count_1)
#---------------------------------------------------
# 3.
# deimpartit = 7
# impartitor = 3
# factor_scalare = 10 ** 100
# deimpartit_nou = deimpartit * factor_scalare

# rezultat = deimpartit_nou // impartitor
# res = str(rezultat)
# parte_int = res[:-100]
# parte_frac = res[-100:]

# print(f"Rezultatul este {parte_int},{parte_frac}")
#---------------------------------------------------
# 6.
import math

def factorial_repr(n):
    factors = []
    i = 1
    while n > 0:
        factors.append(n % i)
        n //= i
        i += 1
    return factors

def nth_permutation(word, n):
    length = len(word)
    
    if n < 0 or n >= math.factorial(length):
        return "Invalid 'n'"
    
    factors = factorial_repr(n)
    word_list = list(word)
    result = []

    for factor in factors[::-1]:
        result.append(word_list.pop(factor))

    return ''.join(result)

word = "abc"
n = 5
print(nth_permutation(word, n))
#---------------------------------------------------
# 7.
# def hex_matrix(hex_string):
#     rows = hex_string.split('\n')
#     for row in rows:
#         hex_nums = row.strip().split(', ')
#         binary_matrix = []

#         for hex_num in hex_nums:
#             hex_int = int(hex_num, 16)
#             bin_num = bin(hex_int)[2:].zfill(8)
#             binary_matrix.extend([int(bit) for bit in bin_num])

#         while len(binary_matrix) < 8 * 16:
#             binary_matrix.append(0)

#         for i in range(0, 8 * 16, 8):
#             print(binary_matrix[i:i + 8])

# hex_string = """0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00
#    0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00
#    0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00
#    0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00
#    0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00
#    0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00"""

# hex_matrix(hex_string)