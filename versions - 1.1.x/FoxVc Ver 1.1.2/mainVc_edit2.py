# -*- coding: utf-8 -*-
import os
import hashlib
import cureVirus as cv

FSL = []  # FileSizeList
FHL = []  # FileHashList
FNL = []  # FileNsmeList
DATABASE = "main.hdb" # DATABASE path
MEMORY = 100000 # DB 파일 읽을때 파일이 작지 않아서 읽어올 때 시간좀 걸리는데 메모리 여유되시는 만큼 적당히 잡으시면됩니다.

HML = []  # Hash Matching-List
SML = []  # Size Matching-List, not used.

INFECTION = [] # hash/size 모두 매칭되는경우


def DS():
    """
    스캔대상 드라이브 문자를 입력받고,
    입럭 받은 디렉토리가 존재하는지 확인.
    :return:
    """
    input_txt = raw_input("Select your Directory which you want to Scan(e.x C) : ")
    drive_txt = str(input_txt) + ":\\" # 윈도우에서 사용하는 경우, 구분자(separator) '\' 가 있어야 경로로 인식(e.g C:\\home\workspace)
    dirS = os.path.abspath(drive_txt)
    if os.path.isdir(dirS):
        print("[+] Ready for Scan Dirve : ", dirS)
        return dirS

    else:
        print("It is not Drive or your system doesn't have", dirS,"Drive")
        return False


def FS(disS):
    """
    File Scan Start
    :param fname:
    :return:
    """
    TFL = []  # TargetFileList
    print("[+]" , disS ,"File Scan Start")

    for (path, dir, files) in os.walk(disS):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            print("%s\%s" % (path, filename))
            TFL.append("%s\%s" % (path, filename))

    return TFL


# 파일 사이즈 비교 루틴
def CFS(fname):
    fsize = os.path.getsize(fname)
    for size in FSL:
        if fsize == size:
            INFECTION.append(fname)
            print("\t[+] File Size is Correct")
            return 1

    print("\t[-] File Size is not Correct")
    return 0

# 파일 md5해시 비교 루틴

def MHV(fname):
    try:
        with open(fname, 'rb') as f: # 입력받은 fname은 C:\\ 이므로 해당 파일이 아니라 열 수 없음...
            buf = f.read()
            md5 = hashlib.md5()
            md5.update(buf)
            fmd5 = md5.hexdigest()
            for hashValue in FHL:
                if fmd5 == hashValue:
                    HML.append(fname)
                    print("\t\t[+] " + fname + " is Virus File")
                    return 1

            print("\t\t[-] " + fname + " is Not Virus File")
        return 0

    except IOError as e:
        print("IOError : Permission or No such file/dir")
        print(e.message)
        return False





def DK():
    """
    악성코드가 생성한 디렉토리를 삭제하는 모듈

    :return:
    """
    for root, dirs, files in os.walk(dir):
        for file in files:
            if (FS(str(root) + "\\" + file)):
                print("\n======== delete ========\n" + str(root) + file + "\n")
                cv.deleteFile(str(root) + "\\" + file)




def run():
    dirS = DS()
    if dirS:
        TFL = FS(dirS) # get target-file list
        for fname in TFL:
            MHV(fname) # set Hash matching list
            for target in HML:
                CFS(target) # set INFECTION
    #end scan-job

    from pprint import pprint
    print("[Infect file list]")
    pprint(INFECTION)

    # 이후 infection 을 기준으로 치료 또는 삭제(사용자선택 등)




if __name__ == "__main__":
    with open(DATABASE, "rb") as fdb: # with문과 함께 작성하면 자동으로 close 해줌
        for hdb in fdb.readlines(MEMORY): # MEMORY 변수 최상단 참고
            hdb = hdb.strip()
            FSL.append(int(hdb.split(':')[0]))
            FHL.append(str(hdb.split(':')[1]))
            FNL.append(str(hdb.split(':')[2]))
            fdb.close()
        #ed for
    #ed open
    run()

