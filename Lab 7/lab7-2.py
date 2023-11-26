import os

def rename_files(dir_path):
    index = 1
    try:
        if not os.path.isdir(dir_path):
            raise ValueError("Path invalid catre director.")
        
        for fis in os.listdir(dir_path):
            file_path = os.path.join(dir_path, fis)
            _,ext = os.path.splitext(fis)
            new_name = "file" + str(index) + ext
            new_file = os.path.join(dir_path, new_name)
            os.rename(file_path, new_file)
            index += 1
    except Exception as e:
        print(f"Eroare: {e}")

rename_files("C:\\Users\\Mihnea\\Desktop\\py")