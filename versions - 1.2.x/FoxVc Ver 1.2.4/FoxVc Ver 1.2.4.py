# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import os
import hashlib
# import cureVirus as cv

File_Size_List = []
File_Hash_List = []
File_Name_List = []

DB = "main.mdb" # maleware DB
memory = 100000

Hash_Matching_List = []
Size_Matching_List = []

INFECTION = [] # hash/size 모두 매칭되는 경우

blacklist = ["bin"] # 휴지통을 블랙리스트로 넣음


# 윈도우 디렉토리 받아서 루틴에 처리
def isDir(): 
	input_txt = raw_input("Select your Directory which you want to Scan(e.x C) :")
	dirve_txt = str(input_txt) + ":\\" # 윈도우에서 사용하는 경우, 구분자(separator) '\'가 있어야 경로로 인식(e.g C:\\home\\workspace)
	dirS = os.path.abspath(dirve_txt)
	if os.path.isdir(dirS): # 만약 입력받은 디렉토리가 존재한다면...
		print("[+] Ready for Scan Drive : ", dirS) # 스캔 준비를 알림.
		return dirS
		
	else:
		print("It si not Drive or your system doesn't have", dirS,"Drive") # 존재하지 않는다면 오류문 출력
		return False


# 파일 스캔을 위한 준비
def File_Scan(dirS):
	Target_File_List = []
	print("[+]", dirS,"File Scan Start") # 입력받은 디렉토리 스캔을 시작함을 알림
	
	for(path, dir, file) in os.walk(dirS): # 모든 디렉토리 불러오기
		for filename in files:
			ext = os.path.splitext(filename)[-1]
			print("%s\%s" % (path, filename))
			Target_File_List.append("%s\%s" % (path, filename))
			
	return Target_File_List
	
	
	
# 악성코드 DB와 불러온 파일을 md5해시화 하여 비교하는 루틴.
def Matching_Hash_Value(fname):
    try:
        with open(fname, 'rb') as f: # 입력받은 fname은 C:\\ 이므로 해당 파일이 아니라 열 수 없음...
            buf = f.read() # 불러들인 것을 buf 변수로 정의함.
            md5 = hashlib.md5()
            md5.update(buf)
            fmd5 = md5.hexdigest()
			if "bin" in blacklist:
				print("this is a blacklist file!")
				for hashValue in File_Hash_List: # for문으로 리스트를 돌림.
                	if fmd5 == hashValue:  # 만약 파일의 md5해시가 멀웨어 DB에 존재한다면..
                    	INFECTION.append(fname) # INFECTION 리스트에 추가함.
                    	Hash_Matching_List.append(fname) # 해시매칭리스트에 추가함.
                    	print("\t\t[+] " + fname + " is Virus File") # 일치한다면 바이러스 파일이라고 출력.
                    return 1

           			 print("\t\t[-] " + fname + " is Not Virus File") # 일치하지 않는다면 바이러스 파일이 아니라고 출력.
        		return 0
# 에러 구문 출력
    except IOError as e: #에러를 선언하고, 에러가 생기면 지정된 구문을 출력
        print("IOError : Permission or No such file/dir")
        print(e.message)
        return False

# 실행 함수.
def run():
	for fanme in File_Scan(isDir()):
		INFECTION += Hash_Matching_List
	
	from pprint import pprint
	print("[Infection File List]")
	pprint(INFECTION)
	
	if INFECTION:
		if str(raw_input("Cure the Virus Now? [y,n] : ")) == "y":
			for infectedFileName in INFECTION: # for문으로 리스트를 돌려서 삭제
				os.remove(file) # 리스트 내의 경로를 삭제함.
				print("[+] Virus File Removed") # 삭제 완료시 이 구문 출력
		else:
			print("[-] Your System Will be Danger. Virus File is still exist.") # 기타 구문을 입력 받으면 삭제 모듈을 취소하고, 구문 출력.
	

	
# DB를 잘라서 구분하는 부분.
if __name__ == "__main__":
	with open(DB, "rb") as fdb: # DB를 불러옴.
		for mdb in fdb.readlines(memory): # 지정된 메모리 안에서 DB를 불러옴.
			mdb = mdb.strip()
			File_Size_List.append(int(mdb.split(':')[0])) # DB에서 맨 앞부분(파일용량)부분만 잘라서 FSL(FileSizeList)에 추가
			# File_Hash_List.append(str(mdb.split(':')[1])) # DB에서 두번째 부분(파일md5해시)부분만 잘라서 FHL(FileHashList)
            File_Name_List.append(str(mdb.split(':')[2])) # DB에서 세번째 부분(파일 이름)부분 잘라서 FNL(FileNAmeList)
            fdb.close()
    run()
	
		
	
			
	
