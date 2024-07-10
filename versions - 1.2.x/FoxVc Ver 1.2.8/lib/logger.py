# -*- coding: utf-8 -*-
# Author : github.com/miho030

import logging, logging.handlers
import os, sys
import datetime, time


# Set log conf
def LoggingConfigure():
	now = datetime.datetime.now()
	nowDate = now.strftime('%Y%m%d')  # ex. 20160621

	log_path = "./log/"
	log_file = nowDate+"_FoxVc.log"

	logger = logging.getLogger('FoxVc')
	
	logPath = os.path.join(os.getcwd(), "./log")
	if not os.path.exists(logPath): os.makedirs(logPath)

	log_file_path = log_path + log_file
	#print log_file_path

	logger.setLevel(logging.INFO)
	formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] [%(module)-16s] --- %(message)s", "%Y-%m-%d %H:%M:%S")
	fileMaxByte = 1024 * 1024 * 10
	rotateHandler = logging.handlers.RotatingFileHandler(log_file_path, maxBytes=fileMaxByte, backupCount=100)
	streamHandler = logging.StreamHandler()
	rotateHandler.setFormatter(formatter)
	logger.addHandler(rotateHandler)
	logger.addHandler(streamHandler)  # console logger

	logger.info("")
	msg = "Start to log-record in '" + str(os.path.abspath(log_file_path)) + "'"
	logger.info(msg)

	return logger


if __name__=="__main__":
	pass


