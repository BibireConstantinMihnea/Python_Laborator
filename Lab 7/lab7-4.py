import os
import sys

def ext_count(dir_path):
    extensions = {}
    try:
        if not os.path.isdir(dir_path):
            raise ValueError("Directorul nu exista.")
        
        for fis in os.listdir(dir_path):
            file_path = os.path.join(dir_path, fis)
            if os.path.isfile(file_path):
                _,extension = os.path.splitext(file_path)
                if extension in extensions:
                    extensions[extension] += 1
                else: extensions[extension] = 1

        for ext, count in extensions.items():
            print(f"Extensia: {ext} #Aparitii: {count}")

    except Exception as e:
        print(f"Eroare: {e}")

path = sys.argv[1]
ext_count(path)