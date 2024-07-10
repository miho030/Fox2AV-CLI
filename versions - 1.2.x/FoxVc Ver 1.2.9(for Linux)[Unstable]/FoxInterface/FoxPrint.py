# -*- coding: utf-8 -*-
# Author : github.com/miho030

from Foxcore import FOX_NAME


def fprint(txt):
	print("[%s] %s" %(FOX_NAME, str(txt)))

def fraw_input(txt):
	return raw_input("[%s] %s" % (str(FOX_NAME), str(txt)))

def finput(txt):
	return input("[%s] %s" % (str(FOX_NAME), str(txt)))