# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com


import os
import hashlib
# import cureVirus as cv

FSL = []  # FileSizeList
FHL = []  # FileHashList
FNL = []  # FileNsmeList
DATABASE = "main.mdb" # DATABASE path
MEMORY = 100000 # DB 파일 읽을때 파일이 작지 않아서 읽어올 때 시간좀 걸리는데 메모리 여유되시는 만큼 적당히 잡으면 되는듯.

HML = []  # Hash Matching-List
SML = []  # Size Matching-List, not used.

INFECTION = [] # hash/size 모두 매칭되는경우


# 윈도우 디렉토리 입력 받아서 루틴에 처리
def DS():
    input_txt = raw_input("Select your Directory which you want to Scan(e.x C) : ")
    drive_txt = str(input_txt) + ":\\" # 윈도우에서 사용하는 경우, 구분자(separator) '\' 가 있어야 경로로 인식(e.g C:\\home\workspace)
    dirS = os.path.abspath(drive_txt)
    if os.path.isdir(dirS): # 만약 입력 받은 디렉토리가 존재한다면..
        print("[+] Ready for Scan Dirve : ", dirS)
        return dirS   # 경로를 리턴

    else:
        print("It is not Drive or your system doesn't have", dirS,"Drive") # 존재하지 않는다면 오류문 출력
        return False

# 파일 스캔을 위한 준비
def FS(disS):
    TFL = []  # TargetFileList
    print("[+]" , disS ,"File Scan Start") # 입력 받은 디렉토리 스캔을 시작함을 알림.

    for (path, dir, files) in os.walk(disS): # 모든 디렉토리 불러오기
    dir[:] = [dirS for dirS in dir if dirS != "C:/$recycle.bin"]
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            print("%s\%s" % (path, filename))
            TFL.append("%s\%s" % (path, filename))

    return TFL

# 이부분에서 리싸이클 빈(휴지통)을 예외처리 해야하는데 어떻게 해야할지...T.T
# 파일을 모두 불러들여 md5해시로 변환하고, 멀웨어 DB와 연동하여 비교시키는 루틴
def MHV(fname):
    try:
        with open(fname, 'rb') as f: # 입력받은 fname은 C:\\ 이므로 해당 파일이 아니라 열 수 없음...
            buf = f.read() # 불러들인 것을 buf 변수로 정의함.
            md5 = hashlib.md5()
            md5.update(buf)
            fmd5 = md5.hexdigest()
            for hashValue in FHL: # for문으로 리스트를 돌림.
                if fmd5 == hashValue:  # 만약 파일의 md5해시가 멀웨어 DB에 존재한다면..
                    INFECTION.append(fname) # INFECTION 리스트에 추가함.
                    HML.append(fname) # 해시매칭리스트에 추가함.
                    print("\t\t[+] " + fname + " is Virus File") # 일치한다면 바이러스 파일이라고 출력.
                    return 1

            print("\t\t[-] " + fname + " is Not Virus File") # 일치하지 않는다면 바이러스 파일이 아니라고 출력.
        return 0
# 에러 구문 출력
    except IOError as e: #에러를 선언하고, 에러가 생기면 지정된 구문을 출력
        print("IOError : Permission or No such file/dir")
        print(e.message)
        return False

def CFS(fname):  #Check File Size임. 파일의 사이즈를 os.path.getsize()로 구한다. 하지만 지금은 쓰이지 않음. 효율성 0.
    pass

# 디렉토리 불러들여 삭제하는 모듈. 사용하지 않을듯함.
# 여기서 recycle.bin을 예외처리 했으나, 예외처리 되지 않음. 왜지..
def DK(): # 모듈 삭제 부분 하지만 지금은 쓸모가 없을 듯함. 이미 INFECTION 목록에서 삭제하는 부분을 만들고 있음.
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


def INPUT_DATA():
        return (str(raw_input("Cure the Virus Now? [y,n] : ")))

if INFECTION:
    if INPUT_DATA() == "y":
        os.remove(file) # 바로 이 부분입니다. 이 부분에 INFECT 리스트를 삭제하도록 하고 싶은데 어떻게 구현해야하는지 모르겠습니다.. ㅠㅠ
        print("[+] Virus File Removed")
    else:
        print("[-] Your System Will be Danger. Virus File is still exist.")


if __name__ == "__main__":
    with open(DATABASE, "rb") as fdb: # with문과 함께 작성하면 자동으로 close 해줌
        for mdb in fdb.readlines(MEMORY): # MEMORY 변수 최상단 참고
            mdb = mdb.strip()
            FSL.append(int(mdb.split(':')[0])) # DB에서 맨 앞부분(파일용량)부분만 잘라서 FSL(FileSizeList)에 추가
            FHL.append(str(mdb.split(':')[1])) # DB에서 두번째 부분(파일md5해시)부분만 잘라서 FHL(FileHashList)
            FNL.append(str(mdb.split(':')[2])) # DB에서 세번째 부분(파일 이름)부분 잘라서 FNL(FileNAmeList)
            fdb.close()
        #ed for
    #ed open
    run()

    