# -*- coding: utf-8 -*-

# Author : github/miho030
# Email : miho0_0@naver.com

import os
import sys
import time
import hashlib

if os.name == 'nt':
    from ctypes import wintypes

from pprint import pprint as pp

# core
from Foxcore.isDir import isDir
from Foxcore.fileScan import File_Scan
from Foxcore.matchingHashValue import Matching_Hash_Value
from Foxcore.FoxDBinfor import DB_Pattern

# interface
from FoxInterface.Logo import print_FoxVclogo

from FoxInterface.FoxConst import Fox_ACTION_IGNORE
from FoxInterface.FoxConst import Fox_ACTION_DISINFECT
from FoxInterface.FoxConst import Fox_ACTION_DELETE
from FoxInterface.FoxConst import Fox_ACTION_QUIT

# lib
from lib.logger import LoggingConfigure
from lib.scanlogger import ScanLoggingConfigure

# global variable
File_Size_List = []
File_Hash_List = []
File_Name_List = []

DB_PATH = "./Foxdb/main.hdb"  # maleware DB
memory = 1024 * 100  # 102400

Hash_Matching_List = []  # 해시 매칭 리스트
Value_Matching_List = []  # 추가적인 검사 매칭 리스트

INFECTION = []  # 감염 파일 리스트
N_INFECTION = []  # 감염 파일이 아닌 리스트


def run():
    # set logger
    logger = LoggingConfigure()
    slogger = ScanLoggingConfigure()

    # print logo
    print_FoxVclogo()  # 로고 UI 출력

    # DB 불러오기
    DB_Pattern()  # DB정리 함수 임포트

    # process
    dirS = isDir()
    if not dirS == False:
        logger.info("Ready for Scan Drive : %s" % str(dirS))
        slogger.info("[+] Ready for Scan Drive : %s" % str(dirS))

        for fname in File_Scan(dirS):
            if not Matching_Hash_Value(fname, File_Hash_List) == 1:
                INFECTION.append(fname)
                continue
            else:
                N_INFECTION.append(fname)

    # for test
    # INFECTION.append("E:\\bak\\sample.txt")



    for infect in INFECTION:
        logger.info("Detected Virus file : '%s'" % (infect))
        slogger.info("\t\t[-] Detected Virus file : '%s'" % (infect))

    if not INFECTION:
        logger.info("[+] Cannot detect Virus !")  # 악성코드가 탐지되지 않았음을 시스템 관리자에게 알림
        slogger.info("[+] Cannot detect Virus !")
        for file in N_INFECTION:
            slogger.info("\t\t[-] This file is not Virus : '%s'" % str(file))


    else:
        time.sleep(1)
        if str(raw_input("Cure the Virus Now? [y,n] : ")) == "y":  # 관리자에게 악성코드 치료 여부 질의
            logger.info("Virus File Removed")  # 삭제 완료시 이 구문 출력
            slogger.info("[+] Virus File Removed")  # 삭제 완료시 이 구문 출력

            for infectedFileName in INFECTION:  # for문으로 리스트를 돌려서 삭제
                os.remove(infectedFileName)  # 리스트 내의 경로를 삭제함.
                logger.info("Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력
                slogger.info("\t\t[-] Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력

        else:
            logger.info("Your System Will be Danger. Malwares are still exist.")  # 악성코드 방치시 위험성에 대해 경고
            slogger.info("\t\t[-] Your System Will be Danger. Virus File is still exist.")  # 로그


# 악성코드 검사 결과 출력

def print_result(result):
    # print
    # print

    from FoxInterface.Color import cprint  # UI 색깔 임포트
    cprint('Results:\n')


if __name__ == "__main__":
    run()





