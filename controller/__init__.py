import os
import pathlib
import sys,glob

file_names = []
path = r"C:\Users\mohan\Desktop\Flask\REST_API with FLASK\controller"
for filename in os.listdir(path):
    if filename.endswith(".py"):
        filename_without_extension = os.path.splitext(filename)[0]
        file_names.append(filename_without_extension)

__all__ = file_names