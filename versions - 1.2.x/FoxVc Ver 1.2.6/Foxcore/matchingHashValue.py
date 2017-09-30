# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import hashlib
import logging

def Matching_Hash_Value(fname, File_Hash_List):
	logger = logging.getLogger("FoxVc")
	slogger = logging.getLogger("Scan")
	blacklist = ["bin", "BIN", "$RECYCLE", "$RECYCLE.BIN"]  # 휴지통을 블랙리스트로 넣음


	try:
		# 불러들인 것을 buf 변수로 정의함.
		with open(fname, 'rb') as f:
			buf = f.read()
			md5 = hashlib.md5()
			md5.update(buf)
		# end with-open

		fmd5 = md5.hexdigest()

		for hashValue in File_Hash_List: # for문으로 리스트를 돌림.
			if fmd5 == hashValue:  # 만약 파일의 md5해시가 멀웨어 DB에 존재한다면..
				#INFECTION.append(fname) # INFECTION 리스트에 추가함.
				return 1

		return 0

	except IOError as e:
		logger.error("IOError : Permission denied. / No such file or directory.")
		logger.error(e.message)

	finally:
		pass
