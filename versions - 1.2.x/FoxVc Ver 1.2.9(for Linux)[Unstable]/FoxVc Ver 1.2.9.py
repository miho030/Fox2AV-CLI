# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import os
import sys
import time

if os.name == 'nt':
    from ctypes import wintypes

from pprint import pprint as pp

# core
from Foxcore.isDir import isDir
from Foxcore.fileScan import File_Scan
from Foxcore.matchingHashValue import Matching_Hash_Value

# interface
from FoxInterface.Logo import print_FoxVclogo

from FoxInterface.FoxConst import Fox_ACTION_IGNORE
from FoxInterface.FoxConst import Fox_ACTION_DISINFECT
from FoxInterface.FoxConst import Fox_ACTION_DELETE
from FoxInterface.FoxConst import Fox_ACTION_QUIT

# lib
from lib.logger import LoggingConfigure
from lib.scanlogger import ScanLoggingConfigure

#=======================================================================================
# 주요 상수 선언
#=======================================================================================
FOX_VERSION = '1.2.9'
FOX_BUILDDATA = '2017'
FOX_LASTYEAR = FOX_BUILDDATA[len(FOX_BUILDDATA)-4:]

# global variable
File_Size_List = []
File_Hash_List = []
File_Name_List = []

DB_PATH = "./Foxdb/main.hdb" # maleware DB
memory = 1024 * 100 # 102400

Hash_Matching_List = [] # 해시 매칭 리스트
Value_Matching_List = [] # 추가적인 검사 매칭 리스트

INFECTION = [] # 감염 파일 리스트
N_INFECTION = [] # 감염 파일 리스트
#INFECTION.append("E:\\bak\\Eicar.txt")



def run():
	# Starting main module.

	# set logger
	logger = LoggingConfigure()
	slogger = ScanLoggingConfigure()

	# run script as root.

	# Ensure that root privileges are granted.
	if not os.geteuid() == 0:
		sys.exit("* Warning *\n\nOnly root can run FoxVc Ver 1.2.9\n")
	else:
		pass

	# Reqeusting to Root Permission.

	euid = os.geteuid()
	if euid != 0:
		print "Script not started as root. Running sudo.."
		args = ['sudo', sys.executable] + sys.argv + [os.environ]
		# the next line replaces the currently-running process with the sudo
		os.execlpe('sudo', *args)

		print 'Running. Your euid is', euid
	pass
	pass
	pass
	pass
	pass
	pass

	# print logo
	print_FoxVclogo()  # 로고 UI 출력

	# DB를 불러옴.
	with open(DB_PATH, "rb") as fdb:
		for hdb in fdb.readlines(memory):  # 지정된 메모리 안에서 DB를 불러옴. >> 정확한 내용은 모르겠으나, DB사이즈가 메모리 범위 밖이여도 상관없는 듯...
			hdb = hdb.split("\n")[0]
			File_Hash_List.append(str(hdb.split(':')[0]))  # DB에서 두번째 부분(파일md5해시)부분만 잘라서 FHL(FileHashList)
			File_Size_List.append(int(hdb.split(':')[1]))  # DB에서 맨 앞부분(파일용량)부분만 잘라서 FSL(FileSizeList)에 추가
			File_Name_List.append(str(hdb.split(':')[2]))  # DB에서 세번째 부분(파일 이름)부분 잘라서 FNL(FileNAmeList)
		# fdb.close()  >> with 문과 함께 사용하므로 close 따로 작성할 필요 없음.

	# process
	dirS = isDir()
	if not dirS==False:
		logger.info("Ready for Scan Drive : %s" % str(dirS))
		slogger.info("[+] Ready for Scan Drive : %s" % str(dirS))

		for fname in File_Scan(dirS):

			if not Matching_Hash_Value(fname, File_Hash_List) == 1:
				N_INFECTION.append(fname)
				continue
			else:
				INFECTION.append(fname)

	# for test
	# INFECTION.append("E:\\bak\\sample.txt")

	for infect in INFECTION:
		logger.info("Detected Virus file : '%s'" % (infect))
		slogger.info("\t\t[-] Detected Virus file : '%s'" %(infect))


	if not INFECTION:
		logger.info("Cannot detect Virus !")
		slogger.info("[+] Cannot detect Virus !")
		for file in N_INFECTION:
			slogger.info("\t\t[-] This file is not Virus : '%s'" % str(file))


	else:
		time.sleep(1)
		if str(raw_input("Cure the Virus Now? [y,n] : ")) == "y":
			logger.info("Virus File Removed")  # 삭제 완료시 이 구문 출력
			slogger.info("[+] Virus File Removed")  # 삭제 완료시 이 구문 출력

			for infectedFileName in INFECTION: # for문으로 리스트를 돌려서 삭제
				os.remove(infectedFileName) # 리스트 내의 경로를 삭제함.
				logger.info("Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력
				slogger.info("\t\t[-] Removed file : %s" % (infectedFileName))  # 삭제 완료시 이 구문 출력

		else:
			logger.info("Your System Will be Danger. Virus File is still exist.")
			slogger.info("\t\t[-] Your System Will be Danger. Virus File is still exist.")

# 악성코드 검사 결과 출력

def print_result(result):

	# print
	# print

	from FoxInterface.Color import cprint  # UI 색깔 임포트
	cprint('Results:\n')

if __name__ == "__main__":
	run()
	
		
	
			
	
