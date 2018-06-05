import os
import sys
from os.path import basename

path = os.path.abspath(sys.argv[1])
parent_folder = path.split('/')[-1]
x = 1
files = sorted(os.listdir(path),key=os.path.getctime)
for file in files:
    if not file.startswith('rename'):
      os.rename(file, str(x) + "_" + parent_folder)
      x += 1
