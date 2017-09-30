# -*- coding: utf-8 -*-
import os
import hashlib
import cureVirus as cv

FSL = []  # FileSizeList
FHL = []  # FileHashList
FNL = []  # FileNsmeList


# 멀웨어 DB 임포트 
fdb = open("main.hdb", "rb")  # main.mdb-> 멀웨어 DB 사이즈:md5해시:이름 순으로 구성됨.
for hdb in fdb.readlines():  # DB읽어오기
    hdb = hdb.strip()
    FSL.append(int(hdb.split(':')[0]))  # 사이즈:md5해시:이름 에서 사이즈 부분만 추출
    FHL.append(str(hdb.split(':')[1]))  # 사이즈:md5해시:이름 에서 해시 부분 추출
    FNL.append(str(hdb.split(':')[2]))  # 사이즈:md5해시:이름 에서 이름 부분 추출
    fdb.close()


def DS():
    dirS = (str(raw_input("Select your Directory which you want to Scan(e.x C) : "))) # raw_input으로 스캔할 디렉토리 임력받음
    if os.path.isdir(dirS): # 입럭 받은 디렉토리가 존재하는지 확인
        print"[+] Ready for Scan Dirve : ", dirS # 존재한다면 프린트문 출력
        return dirS

    else:
        print "It is not Drive or your system doesn't have", dirS,"Drive"  # 존재하지 않는다면 오류값 출력
        return False

def FS(fname):
    print"[+]" , fname ,"File Scan Start" # 파일 스캔을 시작한다는 구문을 출력
    if (CFS(fname)): #만약 CFS가 참이라면 MHV로 넘어가도록 설정 (이 부분을 잘 모르겠습니다. CFS부분이 참이되면 MHV의 검사 루틴으로 넘어가도록 되어야 되는데..)
        MHV(fname)

        if(MHV(fname)):
            return 1
    return 0

def CFS(fname):  #Check File Size임.
    fsize = os.path.getsize(fname) # 파일의 사이즈를 구함
    for size in FSL:  # 만약 FileSizeList에 파일의 사이즈와 같은 값이 있다면.
        if fsize == size: # 파일의 사이즈와 DB의 사이즈가 같다면...
            print"\t[+] File Size is Correct" # 같다면 이 프린트문 출력
            return 1
    print"\t[-] File Size is not Correct" # 아니라면 이 구문을 출력
    return 0

def MHV(fname):  # MatchHashValue
    f = open(fname, "rb")
    buf = f.read() # 새로운 파일을 읽어옴
    f.close()

    md5 = hashlib.md5() #  파일을 md5해시로 변환
    md5.update(buf)
    fmd5 = md5.hexdigest()
    for hashValue in FHL: # FileHashList에 새로운 해시값이 있는지 확인
        if fmd5 == hashValue:  # 만약 파일이 해시값이 FHL에 존재한다면
            print("\t\t[+] " +  fname + " is Virus File") # 파일의 md5해시가 FHL애의 값과 같을 때 이 구문 출력
            return 1
    print("\t\t[-] " + fname + " is Not Virus File") # 파일의 md5해시가 FHL내의 값과 다를 때 이 구문 출력
    return 0

def DK():  # 악성코드가 생성한 디렉토리를 삭제하는 모듈
    for root, dirs, files in os.walk(dir):
        for file in files:
            if (FS(str(root) + "\\" + file)):
                print("\n======== delete ========\n" + str(root) + file + "\n")
                cv.deleteFile(str(root) + "\\" + file)

fname = DS()
if fname:
    FS(fname)
    CFS(fname)
    MHV(fname)
    DK()
