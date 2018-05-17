import os.path
import re

def search_log(path,t,kw):
    files = os.listdir(path)
    os.chdir(path)
    for file in files:
        file_name =  os.path.basename(file)
        if file_name.find(t):
            with open(file, "r") as f:
                content = f.read(1024 * 1024 * 1024)
            break



