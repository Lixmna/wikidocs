from glob import glob
from os.path import isdir

for x in glob('*') :
    if isdir(x):
        print(x, '<DIR>')
    else:
        print(x)
