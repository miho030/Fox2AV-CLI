# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

# +=======================================================================================+
# 이 파일은 파이썬 2 이상의 버전이 설치되어있는 시스템 사용자를 위한 모듈임.
# Python 2.7.14 기준의 문법으로 작성되었음.
#
#
# 주요 모듈 임포트
# +=======================================================================================+
import os, sys
import datetime, time
from time import sleep
import logging, logging.handlers

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

# lib
from lib.logger import LoggingConfigure
from lib.scanlogger import ScanLoggingConfigure


# +=======================================================================================+
# 주요 변수 선언 시작
# +=======================================================================================+

logger = LoggingConfigure()
slogger = ScanLoggingConfigure()

# global variable
File_Size_List = []
File_Hash_List = []
File_Name_List = []


Hash_Matching_List = [] # 해시 매칭 리스트
Value_Matching_List = [] # 추가적인 검사 매칭 리스트

INFECTION = [] # 감염 파일 리스트
N_INFECTION = [] # 감염 파일 리스트

# +=======================================================================================+
# 주요 변수 선언 끝
# +=======================================================================================+


def FoxVcPyVer2():
    # DB를 불러옴.
    DB_Pattern()

    # process
    dirS = isDir()
    if not dirS == False:
        logger.info("Ready for Scan Drive : %s" % str(dirS))
        slogger.info("[+] Ready for Scan Drive : %s" % str(dirS))

        for fname in File_Scan(dirS):

            if not Matching_Hash_Value(fname, File_Hash_List) == 1:
                N_INFECTION.append(fname)
                continue
            else:
                INFECTION.append(fname)

    for infect in INFECTION:
        logger.info("Detected Virus file : '%s'" % (infect))
        slogger.info("\t\t[-] Detected Virus file : '%s'" % (infect))

    if not INFECTION:
        logger.warning("Cannot detect Virus !")
        slogger.warning("[+] Cannot detect Virus !")
        for file in N_INFECTION:
            slogger.info("\t\t[-] This file is not Virus : '%s'" % str(file))


    else:
        time.sleep(1)
        if str(raw_input("Cure the Virus Now? [y,n] : ")) == "y":
            logger.info("Virus File Removed")  # 삭제 완료시 이 구문 출력
            slogger.info("[+] Virus File Removed")  # 삭제 완료시 이 구문 출력

            for infectedFileName in INFECTION:  # for문으로 리스트를 돌려서 삭제
                os.remove(infectedFileName)  # 리스트 내의 경로를 삭제함.
                logger.warning("Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력
                slogger.warning("\t\t[-] Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력

        else:
            logger.critical("Your System Will be Danger. Virus File is still exist.")
            slogger.critical("\t\t[-] Your System Will be Danger. Virus File is still exist.")


