# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import cureVirus as cv

FSL = []
FHL = []
FNL = []

DATABASE = "main.hdb"
MEMORY = 100000

def DS():
    input_txt = raw_input("Select your Directory which you want to scan(e.x C) :")
    drive_txt = str(input_txt) + ":\\"
    dirS = os.path.abspath(drive_txt)
    if os.path.isdir(dirS):
        print "[+] Ready for Scan Dirve : ", dirS
        return dirS
    else:
        print"[-] It is not Drive or your System doesn't have, dirS, Drive"
        return False

def FS(fname):
    print"[+]", fname,"File Scan Start"
    if (CFS(fname)):
       if (MHV(fname)):
           return 1
           
    return 0
    
def MHV(fname):
    try:
        with open(fname, 'rb') as f:
            buf = f.read()
            md5 = hashlib.md5()
            md5.update(buf)
            fmd5 = md5.hexdigest()
            for hashValue in FHL: 
                if fmd5 == hashValue: 
                    print("\t\t[+] " + fname + " is Virus File") 
                    return 1
            print("\t\t[-] " + fname + " is Not Virus File")  
            return 0

    except IOError as e:
        print("IOError : Permission or No such file/dir")
        print(e.message)
        return False
    
def CFS(fname):
    fsize = os.path.getsize(fname)
    for size in FSL:
        if fsize == size:
            print("\t[+] File Size is Correct")
            return 1

    print("\t[-] File Size is not Correct")
    return 0
            
def DK():
    for root, dirs, files in os.walk(dir):
        for file in files:
            if (FS(str(root) + "\\" + file)):
                print("\n======== delete ========\n" + str(root) + file + "\n")
                cv.deleteFile(str(root) + "\\" + file)


if __name__ == "__main__":
    with open(DATABASE, "rb") as fdb: 
        for hdb in fdb.readlines(MEMORY):
            hdb = hdb.strip()
            FSL.append(int(hdb.split(':')[0]))
            FHL.append(str(hdb.split(':')[1]))
            FNL.append(str(hdb.split(':')[2]))
            fdb.close()

    fname = DS()
    if fname:
        FS(fname)
        CFS(fname)
        MHV(fname)
        DK()

            
