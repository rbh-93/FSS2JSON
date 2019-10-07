import os
import sys
import requests
import configparser

'''
Recursively goes through a directory and 
stores the names, corresponding types (root folder='system', child folders='folder', files='file')
and respective paths in JSON structure. 
The key 'children' has a nested JSON if it is a folder. If a file is encountered the contents of the 
file are stored as a string in the 'children' key.
'''


def path_to_dict(path, child=False):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        if not child:
            d['type'] = "system"
        else:
            d['type'] = "folder"
        d['path'] = os.path.relpath(path).strip('..\\').replace('\\', '/')
        d['children'] = [path_to_dict(os.path.join(path, x), child=True) for x in os.listdir \
            (path)]
    else:
        if not child:
            d['type'] = "system"
        else:
            d['type'] = "file"
        d['path'] = os.path.relpath(path).strip('..\\').replace('\\', '/')
        with open(path, 'r', encoding="utf-8", errors='ignore') as myfile:
            content = myfile.read().splitlines()
        d['children'] = content
    return d



