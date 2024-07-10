# -*- coding: utf-8 -*-
# Author : github.com/miho030

import sys

from Foxcore import FOX_VERSION
from Foxcore import FOX_BUILDDATA
from Foxcore import FOX_LASTYEAR

from FoxInterface.Color import cprint
from FoxInterface.Color import FOREGROUND_GREEN
from FoxInterface.Color import FOREGROUND_INTENSITY

def print_FoxVclogo():
	"""
	백신 로고 정의와 출력
	:return: not used.
	"""

	logo = '''Fox Anti Virus Vaccine (for %s) Ver %s (%s) This Program is made by Nicht.
CopyRight (C) 1995-%s GNU/GPL, Lee Joon Sung
'''

	print '==========================================================================='
	s = logo % (sys.platform.upper(), FOX_VERSION, FOX_BUILDDATA, FOX_LASTYEAR)
	cprint(s, FOREGROUND_GREEN | FOREGROUND_INTENSITY)
	print '==========================================================================='
