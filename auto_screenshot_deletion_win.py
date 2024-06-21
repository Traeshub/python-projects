""" This is a personal script for deleting screenshots out of 
my directory"""

import glob
import os

dir_path = "C:\\Name of your windows file path\\"
file_pattern = "*.png"

file_paths = glob.glob(os.path.join(dir_path,file_pattern))
for file_path in file_paths:
    os.remove(file_path)