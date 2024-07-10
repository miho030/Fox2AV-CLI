# -*- coding: utf-8 -*-

# Author : github/miho030
# Email : miho0_0@naver.com

from Foxcore import FOX_NAME


def fprint(txt):
	print("[%s] %s" %(FOX_NAME, str(txt)))

def fraw_input(txt):
	return raw_input("[%s] %s" % (str(FOX_NAME), str(txt)))

def finput(txt):
	return input("[%s] %s" % (str(FOX_NAME), str(txt)))