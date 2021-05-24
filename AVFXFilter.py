# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:04:37 2020

@author: Silvris
"""
import os

AVFX_files = []
ATEX_files = []

for dirpath, dirname, files in os.walk('D:/FFXIV/0008 index/'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
         with open(f'{dirpath}/{file_name}','rb') as f:
             magic = f.read(4)
             print(magic)
             file_title, ext = os.path.splitext(file_name)
             if magic == b'XFVA':
                 print("AVFX found.")
                 AVFX_files.append(f'{dirpath}/{file_title}{ext}')
             else:
                 print("ATEX found.")
                 ATEX_files.append(f'{dirpath}/{file_title}{ext}')

i = 0

for file in AVFX_files:
    i = i+1
    file_title, og_ext = os.path.splitext(file)
    os.rename(f'{file_title}{og_ext}',f'{file_title}{i}.avfx')

i = 0

for file in ATEX_files:
    i = i+1
    file_title, og_ext = os.path.splitext(file)
    os.rename(f'{file_title}{og_ext}',f'{file_title}{i}.atex')