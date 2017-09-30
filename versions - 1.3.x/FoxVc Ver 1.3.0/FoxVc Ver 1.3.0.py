# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

# +=======================================================================================+
# 주요 모듈 임포트 (사실 각 버전별 최적화된 모듈에서 임포트하므로 사실상 필요없음.)
# +=======================================================================================+
import os, sys
import datetime
from time import sleep
import logging, logging.handlers

if os.name == 'nt':
    from ctypes import wintypes

from pprint import pprint as pp

# core
from Foxcore.isDir import isDir
from Foxcore.fileScan import File_Scan
from Foxcore.matchingHashValue import Matching_Hash_Value

# interface
from FoxInterface.Logo import print_FoxVclogo

# lib
from lib.logger import LoggingConfigure
from lib.scanlogger import ScanLoggingConfigure

# Engine
from FoxVcpy2 import FoxVcPyVer2
from FoxVcpy3 import FoxVcPyVer3


# +=======================================================================================+
# 주요 변수 선언 시작.
# +=======================================================================================+

Hash_Matching_List = [] # 해시 매칭 리스트
Value_Matching_List = [] # 추가적인 검사 매칭 리스트

INFECTION = [] # 감염 파일 리스트
N_INFECTION = [] # 감염 파일 리스트


# +=======================================================================================+
# 백신 엔진 구동 -> 주로 악성코드 탐지와 치료를 위한 모듈들이 임포트됨.
# +=======================================================================================+

def FoxVcRun():
	# Starting main module.

	# set logger
	logger = LoggingConfigure()
	slogger = ScanLoggingConfigure()

	pass
	pass
	pass
	# print logo
	print_FoxVclogo()  # 로고 UI 출력


	# +=======================================================================================+
	# 사용자 시스템에 설치되어 있는 파이썬의 버전을 감지하고 각 버전에 최적화된 모듈 임포트함.
	# +=======================================================================================+

	# 파이썬 버전에 따라 버전에 최적화된 모듈을 실행하는 부분
	# sys모듈을 사용하여 설치된 파이썬 버전을 변수로 지정.

	if sys.version_info[:1] == (2,): # FoxVc을 실행하는 시스템에 파이썬 2.x이 설치된경우.
		print "[!] ", "You have Python2.x!"
		print "[+] ", "Start python 2.x modules...\n"
		FoxVcPyVer2()

	else:
		print "[ + Error + ] ", "Python 2.x is not installed in your system !"
		if sys.version_info[:1] == 3: # FoxVc을 실행하는 시스템에 파이썬 3.x이 설치된경우.
			print ( "[+] ", "You have Python3.x!" )
			print ( "[+]", "Start python 3.x modules...\n" )
			FoxVcPyVer3()
		else:
			print ( " " )
			print ( "+==========================================================================+" )
			print ( "[ - Warning - ] Our FoxVc does not support less than the Python 2 version." )
			print ( "[-] For smooth execution, please install Python version 2 or version 3." )
			print ( "+==========================================================================+" )
			pass


# 악성코드 검사 결과 출력

def print_result(result):

	# print
	# print

	from FoxInterface.Color import cprint  # UI 색깔 임포트
	cprint('Results:\n')

if __name__ == "__main__":
	FoxVcRun()

