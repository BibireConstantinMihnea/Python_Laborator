import sys
import os

def print_files(path, ext):
    try:
        if not os.path.isdir(path):
           raise ValueError("Invalid directory path. Please provide a valid directory path.")
        for fis in os.listdir(path):
            if fis.endswith(ext):
                file_path = os.path.join(path, fis)
                try:
                    f = open(file_path, 'r')
                    print(f"File: {fis} \n Contents: {f.read()}")
                    f.close()

                except Exception as file_error:
                    print(f"Eroare la accesarea {fis}; Error:{file_error}")

    except Exception as e:
        print(f"S-a produs o eroare; Error:{e}")


path = sys.argv[1]
extension = sys.argv[2]
print_files(path, extension)
