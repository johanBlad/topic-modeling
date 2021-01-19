import os

def txtfile_tostring(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def txtdir_tolist(dirpath):
    return [txtfile_tostring(os.path.join(dirpath, filename)) for filename in os.listdir(dirpath)]
