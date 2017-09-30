# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import os, sys
import logging
Pyver=sys.version

# 윈도우 디렉토리 받아서 루틴에 처리
def isDir():
	logger = logging.getLogger("FoxVc")
	slogger = logging.getLogger("Scan")

	if sys.version_info[:1] == (2,):
		print "[+] ", "Python %s has been verified in your system." %Pyver[:3]
		raw_input_txt = raw_input("Select your Directory which you want to Scan(e.x C) :")
		if len(raw_input_txt) == 1:
			dirve_txt = str(raw_input_txt) + ":\\"  # 윈도우에서 사용하는 경우, 구분자(separator) '\'가 있어야 경로로 인식(e.g C:\\home\\workspace)
			dirS = os.path.abspath(dirve_txt)

		else:
			dirS = os.path.abspath(raw_input_txt)

		if os.path.isdir(dirS):  # 만약 입력받은 디렉토리가 존재한다면...
			return dirS

		else:
			logger.error("It is not Drive or your system doesn't have %s Drive" % (str(dirS)))  # 존재하지 않는다면 오류문 출력
			return False
	else:
		print "[-] ", "Python2.x is not installed in your system. Try again scan python version on your system."
		pass

	if not sys.version_info[:1] == (3,):
		print ( "[+] Python %s has been verified in your system." ) % Pyver[:3]
		input_txt = input( "Select your Directory which you want to Scan(e.x C) :")
		if len(input_txt) == 1:
			dirve_txt = str(input_txt) + ":\\"  # 윈도우에서 사용하는 경우, 구분자(separator) '\'가 있어야 경로로 인식(e.g C:\\home\\workspace)
			dirS = os.path.abspath(dirve_txt)

		else:
			dirS = os.path.abspath(input_txt)

		if os.path.isdir(dirS):  # 만약 입력받은 디렉토리가 존재한다면...
			return dirS

		else:
			logger.error("It si not Drive or your system doesn't have %s Drive" % (str(dirS)))  # 존재하지 않는다면 오류문 출력
			return False
	else:
		print ( "\n\n[ + Warning + ] Our FoxVc does not support less than the Python 2 version." )
		print ( "[-] For smooth execution, please install Python version 2 or version 3." )