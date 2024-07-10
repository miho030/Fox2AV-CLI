# -*- coding: utf-8 -*-

# Author : github.com/miho030

#-----------------------------------------------------------------------------------------------------
# DB를 정리하여 루틴에 적용하는 모듈
#-----------------------------------------------------------------------------------------------------

# global variable
File_Size_List = []
File_Hash_List = []
File_Name_List = []

DB_PATH = ".\Foxdb\main.hdb" # maleware DB
memory = 1024 * 100 # 102400


with open(DB_PATH, "rb") as fdb:
    for hdb in fdb.readlines(memory):  # 지정된 메모리 안에서 DB를 불러옴. >> 정확한 내용은 모르겠으나, DB사이즈가 메모리 범위 밖이여도 상관없는 듯...
        hdb = hdb.split("\n")[0]
        File_Hash_List.append(str(hdb.split(':')[0]))  # DB에서 맨 앞부분(파일용량)부분만 잘라서 FSL(FileSizeList)에 추가
        File_Size_List.append(int(hdb.split(':')[1]))  # DB에서 두번째 부분(파일md5해시)부분만 잘라서 FHL(FileHashList)
        File_Name_List.append(str(hdb.split(':')[2]))  # DB에서 세번째 부분(파일 이름)부분 잘라서 FNL(FileNAmeList)
        print(File_Hash_List)