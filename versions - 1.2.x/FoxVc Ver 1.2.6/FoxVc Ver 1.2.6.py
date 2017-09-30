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

# lib
from lib.logger import LoggingConfigure
from lib.scanlogger import ScanLoggingConfigure

#=======================================================================================
# 주요 상수 선언
#=======================================================================================
FOX_VERSION = '1.2.6'
FOX_BUILDDATA = '2017'
FOX_LASTYEAR = FOX_BUILDDATA[len(FOX_BUILDDATA)-4:]

# global variable
File_Size_List = []
File_Hash_List = []
File_Name_List = []

DB_PATH = ".\Foxdb\main.hdb" # maleware DB
memory = 1024 * 100 # 102400

Hash_Matching_List = [] # 해시 매칭 리스트
Value_Matching_List = [] # 추가적인 검사 매칭 리스트

INFECTION = [] # 감염 파일 리스트
N_INFECTION = [] # 감염 파일 리스트

#=======================================================================================
# 콘솔 색깔 출력 위한 클래스와 함수들
#=======================================================================================
FOREGROUND_BLACK = 0x0000
FOREGROUND_BLUE = 0x0001
FOREGROUND_GREEN = 0x0002
FOREGROUND_CYAN = 0x0003
FOREGROUND_RED = 0x0004
FOREGROUND_MAGENTA = 0x0005
FOREGROUND_YELLOW = 0x0006
FOREGROUND_GREY = 0x0007
FOREGROUND_INTENSITY = 0x0008  # foreground color is intensified.

BACKGROUND_BLACK = 0x0000
BACKGROUND_BLUE = 0x0010
BACKGROUND_GREEN = 0x0020
BACKGROUND_CYAN = 0x0030
BACKGROUND_RED = 0x0040
BACKGROUND_MAGENTA = 0x0050
BACKGROUND_YELLOW = 0x0060
BACKGROUND_GREY = 0x0070
BACKGROUND_INTENSITY = 0x0080  # background color is intensified.

NOCOLOR = False  # 색깔 옵션값

if os.name == 'nt': #OS 지정
	from ctypes import windll, Structure, c_short, c_ushort, byref

	SHORT = c_short
	WORD = c_ushort


	class Coord(Structure):
		_fields_ = [
			("X", SHORT),
			("Y", SHORT)]


	class SmallRect(Structure):
		_fields_ = [
			("Left", SHORT),
			("Top", SHORT),
			("Right", SHORT),
			("Bottom", SHORT)]


	class ConsoleScreenBufferInfo(Structure):
		_fields_ = [
			("dwSize", Coord),
			("dwCursorPosition", Coord),
			("wAttributes", WORD),
			("srWindow", SmallRect),
			("dwMaximumWindowSize", Coord)]

	# Winbase.h
	STD_INPUT_HANDLE = -10
	STD_OUTPUT_HANDLE = -11
	STD_ERROR_HANDLE = -12

	stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
	GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo


	def get_text_attr():
		csbi = ConsoleScreenBufferInfo()
		GetConsoleScreenBufferInfo(stdout_handle, byref(csbi))
		return csbi.wAttributes


	def set_text_attr(color):
		SetConsoleTextAttribute(stdout_handle, color)

	def cprint(msg, color):
		if not NOCOLOR:
			default_colors = get_text_attr()
			default_bg = default_colors & 0x00F0

			set_text_attr(color | default_bg)
			sys.stdout.write(msg)
			set_text_attr(default_colors)
		else:
			sys.stdout.write(msg)
			sys.stdout.flush()
else:
	def cprint(msg, color):
		sys.stdout.write(msg)
		sys.stdout.flush()

def print_error(msg):
	cprint('Error: ', FOREGROUND_RED | FOREGROUND_INTENSITY)
	print (msg)


#=======================================================================================
# 백신 로고 정의와 출력
#=======================================================================================

def print_FoxVclogo():
	logo = '''Fox Anti Virus Vaccine (for %s) Ver %s (%s)
CopyRight (C) 1995-%s GNU/GPL, Lee Joon Sung
'''

	print '==========================================================================='
	s = logo % (sys.platform.upper(), FOX_VERSION, FOX_BUILDDATA, FOX_LASTYEAR)
	cprint(s, FOREGROUND_GREEN | FOREGROUND_INTENSITY)
	print '==========================================================================='



def run():
	# set logger
	logger = LoggingConfigure()
	slogger = ScanLoggingConfigure()

	# 로고 출력
	print_FoxVclogo()

	# DB를 불러옴.
	with open(DB_PATH, "rb") as fdb:
		for mdb in fdb.readlines(memory):  # 지정된 메모리 안에서 DB를 불러옴. >> 정확한 내용은 모르겠으나, DB사이즈가 메모리 범위 밖이여도 상관없는 듯...
			mdb = mdb.split("\n")[0]
			File_Size_List.append(int(mdb.split(':')[0]))  # DB에서 맨 앞부분(파일용량)부분만 잘라서 FSL(FileSizeList)에 추가
			File_Hash_List.append(str(mdb.split(':')[1])) # DB에서 두번째 부분(파일md5해시)부분만 잘라서 FHL(FileHashList)
			File_Name_List.append(str(mdb.split(':')[2]))  # DB에서 세번째 부분(파일 이름)부분 잘라서 FNL(FileNAmeList)
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
	#INFECTION.append("E:\\bak\\sample.txt")



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

	print
	print

	cprint('Results:\n')

if __name__ == "__main__":
	run()
	
		
	
			
	
