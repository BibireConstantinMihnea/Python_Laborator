#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#                                                         O
#[100G,50G) [50G,10G) [1G,100M) [100M,10M) [1M,100K) [100K,10K)
#---------------------------------------------------------------------------------
import os
import sys

# print(len(sys.argv))
# print(sys.argv)


# f = open('fisier.txt', 'r')
# data = f.read()
# f.close()

# with open('fisier.txt', 'r') as f:
#     data = f.read()

# f = open('fisier.txt', 'w')
# data = f.write('\n')
# f.close()

# with open('fisier.txt', 'w') as f:
#     data = f.write('something')


# files = os.listdir('c:\\')
# print(files)

# for fis in os.listdir('c:\\'):
#     pabs = os.path.join('c:', fis)
#     if os.path.isfile(pabs):
#         size = os.path.getsize(pabs)
#         print(pabs, ' is file : ', size / (2**20), 'MB')
#     else: print(pabs, ' is folder')

def get_file_info():
    f = open("files.txt", 'w')
    for fis in os.listdir('c:\\'):
        pabs = os.path.join('C:\\', fis)
        if os.path.isfile(pabs):
            size = os.path.getsize(pabs)
            cat, size = size_category(size)
            f.write(f"Path: {pabs} , Size: {size} , Size Category: {cat}\n")
    f.close()

def size_category(size):
    if size >= 100 * 2**30:
        return "[100G+)", f"{size / 2 ** 30} GB"
    elif size >= 50 * 2**30:
        return "[50G,100G)", f"{size / 2 ** 30} GB"
    elif size >= 10 * 2**30:
        return "[10G,50G)", f"{size / 2 ** 30} GB"
    elif size >= 1 * 2**30:
        return "[1G,10G)", f"{size / 2 ** 30} GB"
    elif size >= 100 * 2**20:
        return "[100M,1G)", f"{size / 2 ** 20} MB"
    elif size >= 10 * 2**20:
        return "[10M,100M)", f"{size / 2 ** 20} MB"
    elif size >= 1 * 2**20:
        return "[1M,10M)", f"{size / 2 ** 20} MB"
    elif size >= 100 * 2**10:
        return "[100k,1M)", f"{size / 2 ** 10} KB"
    elif size >= 10 * 2**10:
        return "[10k,100k)", f"{size / 2 ** 10} KB"
    else:
        return "[0,10k)", f"{size} KB"

def build_histogram():
    for fis in os.listdir('c:\\'):
        pabs = os.path.join('C:\\', fis)
        if os.path.isfile(pabs):
            size = os.path.getsize(pabs)
            cat, _ = size_category(size)
            if cat == "[0,10k)": print("                                                                  O")
            elif cat == "[10k,100k)": print("                                                        O")
    print("[100G,50G) [50G,10G) [1G,100M) [100M,10M) [1M,100K) [100K,10K) [0,10k]")

get_file_info()
build_histogram()