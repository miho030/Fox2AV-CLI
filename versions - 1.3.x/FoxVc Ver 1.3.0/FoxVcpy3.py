# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import os
import sys
import time
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

INFECTION = [] # 감염 파일 리스트
N_INFECTION = [] # 감염 파일 리스트


def FoxVcPyVer3():
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
        logging.info("Detected Virus file : '%s'" % (infect))
        logging.info("\t\t[-] Detected Virus file : '%s'" % (infect))

    if not INFECTION:
        logging.warning("Cannot detect Virus !")
        logging.warning("[+] Cannot detect Virus !")
        for file in N_INFECTION:
            logging.info("\t\t[-] This file is not Virus : '%s'" % str(file))


    else:
        time.sleep(1)
        if str(raw_input("Cure the Virus Now? [y,n] : ")) == "y":
            logging.info("Virus File Removed")  # 삭제 완료시 이 구문 출력
            logging.info("[+] Virus File Removed")  # 삭제 완료시 이 구문 출력

            for infectedFileName in INFECTION:  # for문으로 리스트를 돌려서 삭제
                os.remove(infectedFileName)  # 리스트 내의 경로를 삭제함.
                logging.warning("Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력
                logging.warning("\t\t[-] Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력

        else:
            logging.critical("Your System Will be Danger. Virus File is still exist.")
            logging.critical("\t\t[-] Your System Will be Danger. Virus File is still exist.")