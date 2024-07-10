# Author : github.com/miho030
import hashlib
import os
import sys

fname = "G:\\eicar-Test.txt"

with open(fname, 'rb') as f:
    fmd5 = hashlib.md5(f.read()).hecdigest()

print fmd5
