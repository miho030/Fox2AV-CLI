# -*- coding: utf-8 -*-
# Author : github.com/miho030

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