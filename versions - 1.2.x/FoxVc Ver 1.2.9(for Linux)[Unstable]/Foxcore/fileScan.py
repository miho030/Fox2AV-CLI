# -*- coding: utf-8 -*-

# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# Author_Helper : Republic of Korea, KyungGido, Kim Min Seok
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

import os
import logging

def File_Scan(dirS):
	slogger = logging.getLogger("Scan")
	Target_File_List = []

	for (path, dir, files) in os.walk(dirS):  # 모든 디렉토리 불러오기
		for filename in files:
			ext = os.path.splitext(filename)[-1]
			#slogger.info("%s\%s" % (path, filename))
			Target_File_List.append("%s\%s" % (path, filename))

	return Target_File_List