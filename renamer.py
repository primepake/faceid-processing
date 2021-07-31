import os
import pathlib
import random
import argparse

parser = argparse.ArgumentParser(description='Rename folders containing collected data according to => Name_Surname => formatting')
# general
parser.add_argument('--data-dir', default='', help='full path to the directory with collected images without formatting of folder names')
args = parser.parse_args()
root = args.data_dir

for path, subdirs, files in os.walk(root):
    i = 1
    print(f'path: {path}')
    print(f'subdirs: {subdirs}')
    subdir = path.split('/')[1]
    for name in files:
        extension = name.split(".")[-1].lower()
        if extension != "jpg":
            continue
        print(f'name: {name}')
        stri = str(random.randint(1,1000))
        stri = stri.zfill(4)
        print(f'stri {stri}')
        source_name = os.path.join(path, name)
        des_name = os.path.join(path, os.path.basename(path) + "_" + stri + '.' + extension)
        os.rename(source_name, des_name)
        i = i + 1
        print(os.path.basename(path))
