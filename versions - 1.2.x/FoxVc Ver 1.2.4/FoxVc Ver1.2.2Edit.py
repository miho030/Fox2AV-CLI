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
"INFECTION이라는 빈 리스트를 먼저 선언했습니다."


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
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            print("%s\%s" % (path, filename))
            TFL.append("%s\%s" % (path, filename))

    return TFL


def MHV(fname):
    try:
        with open(fname, 'rb') as f: # 입력받은 fname은 C:\\ 이므로 해당 파일이 아니라 열 수 없음...
            buf = f.read() # 불러들인 것을 buf 변수로 정의함.
            md5 = hashlib.md5()
            md5.update(buf)
            fmd5 = md5.hexdigest()
            for hashValue in FHL: # for문으로 리스트를 돌림.
                if fmd5 == hashValue:  # 만약 파일의 md5해시가 멀웨어 DB에 존재한다면..
                    INFECTION.append(buf) # INFECTION 리스트에 추가함.
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
        dirs[:] = [dir for dir in dirs if dir != "C:/$recycle.bin"]
        for file in files:
            if (FS(str(root) + "\\" + file)):
                print("\n======== delete ========\n" + str(root) + file + "\n")
                cv.deleteFile(str(root) + "\\" + file)


def run():
    # 이 아래로 3~4줄은 불필요하게 코드가 많이 삽입됐습니다. 그래서 제가 좀 줄여둡니다.
    #dirS = DS() # DS라는 불명확한 이름보다는 isDir 과 같은 명확한 이름이 좋습니다.
    #if dirS: 
    #    TFL = FS(dirS) # get target-file list
    for fname in FS(DS()):
        INFECTION += MHV(fname)  # set Hash matching list
        #for target in HML:
        #    CFS(target)# set INFECTION

            # CFS 내부에 내용이 없네요 --??
            # 불필요한 함수가 너무 많고 함수의 이름이 불명확하여 코드의 가독성이 너무 떨어집니다.
            # MHV--> hash_matching_list() 함수 이름을 역할에 맞게 분명하게 적어주세요!
            # 제 생각엔 해시가 매칭되는 리스트를 가져오면 될듯 합니다. 이때, 이 리스트에는 파일의 full_path를 적어주는게 좋겠습니다.
            # 딱 두줄로 줄였네요 --; 위와 같이
            #     1. 프로그램의 가독성을 높이고
            #     2. 프로그램의 불필요한 부분을 줄이면서(입력값과 리턴값은 유지)
            #     3. 프로그램의 생산성을 높이는 작업
            # 을 리펙토링이라고 부릅니다.
            # 프로그래밍 논리가 어느정도 잡히셨다면
            # http://book.naver.com/bookdb/book_detail.nhn?bid=6871807
            # http://book.naver.com/bookdb/book_detail.nhn?bid=9899036
            # 책들을 읽어보시길 바래요.
            # 그래도 코드가 많이 이뻐졌네요 ㅎㅎㅎ
                
    #end scan-job

    from pprint import pprint
    print("[Infect file list]")
    pprint(INFECTION)
    #여기까지 와서 INFECTION이 다음과 같은 형식이어야 합니다.
    # ['c:\\test.txt', 'c:\\windows\\system32\\notepad.exe']

    if INFECTION:
        "그리고는, md5해시를 비교하고는 내용이 같으면 리스트에 넣는 방식으로 짰습니다."
        if str(raw_input("Cure the Virus Now? [y,n] : ")) == "y":
            for infectedFileName in INFECTION: # for문으로 리스트의 내용을 하나씩 꺼내올 수 있습니다.
                os.remove(file) # 바로 이 부분입니다. 이 부분에 INFECT 리스트를 삭제하도록 하고 싶은데 어떻게 구현해야하는지 모르겠습니다.. ㅠㅠ
                print("[+] Virus File Removed")
        else:
            print("[-] Your System Will be Danger. Virus File is still exist.")


def INPUT_DATA(): # 이런 간단한 내용은 그냥 써주는게 좋습니다. 함수이름은 항상 정확하게!
        return (str(raw_input("Cure the Virus Now? [y,n] : ")))




if __name__ == "__main__":
    # 오히려 데이터 베이스를 세팅하는 이런 것은 함수로 만들어 두면 좋죠 ㅎㅎㅎ
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

    
