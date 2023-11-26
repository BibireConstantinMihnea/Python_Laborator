import os
import sys

def total_size(dir_path):
    total = 0
    try:
        if not os.path.isdir(dir_path):
            raise ValueError("Directorul nu exista.")
        for root, dirs, fis in os.walk(dir_path):
            for file in fis:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    total += os.path.getsize(file_path)

        print(f"Directorul {dir_path} are marimea de: {total} B")

    except Exception as e:
        print(f"Eroare: {e}")

path = sys.argv[1]
total_size(path)