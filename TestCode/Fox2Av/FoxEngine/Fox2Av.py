"""
made by Nicht = tayaka = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong.

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

If you have time, stop by my YouTube channel!  ==> https://www.youtube.com/channel/UC7HDAfqRbKKLONZ9PmAiwtg?view_as=subscriber
just fun! :D

"""

import cgi
import HTMLParser
import cvs
import sml.etree.cElementTree
import json
import email
import yara

import os, sys
import types
import hashlib
import urllib
import time
import struct
import datetime
import FoxCore.FoxEngine
import FoxCore.FoxConst
from optparse import OptionParser

try:
    import pyizma
except ImportError:
    pass

if os.name == 'nt':
    from ctypes import wintypes


FVC_VERSION  = '0.1'
FVC_BUILDDATE = '2018.01.05'
FVC_LASTYEAR = FVC_BUILDDATE[len(FVC_BUILDDATE)-4:]

g_options = None
g_delta_time = None

FORGROUND_BLACK = 0x0000
FORGROUND_BLUE = 0x0001
FORGROUND_GREEN = 0x0002
FORGROUND_CYAN = 0x0003
FORGROUND_red = 0x0004
FORGROUND_MAFENTA = 0x0005
FORGROUND_YELLOW = 0x0006
FORGROUND_GREY = 0x0007
FORGROUND_INTENSITY = 0x0008

BACKGROUND_BLACK = 0x0000
BACKGROUND_BLUE = 0x0010
BACKGROUND_GREEN = 0x0020
BACKGROUND_CYAN = 0x0030
BACKGROUND_RED = 0x0040
BACKGROUND_MAGENTA = 0X0050
BACKGROUND_YELLOW = 0x0060
BACKGROUND_GREY = 0x0070
BACKGROUND_INTENSITY = 0x0080


NOCOLOR = False

if os.name = 'nt':
    from ctypes import windll, Structure, c_short, c_ushort, byref

    SHORT = c_short
    WORD = c_ushort

    class Coord(struture):
        _fields_ = [
            ("X", SHORT),
            ("Y", SHORT)]

    class SmalPect(Structure):
        _fields = [
            ("Left", SHORT),
            ("TOP", SHORT),
            ("RIGHT", SHORT),
            ("Right", SHORT)]

    class ConsoleScreenBufferInfo(Structure):
        _fields = [
            ("dwsize", Coord),
            ("dwCursorPosition", Coord),
            ("wAttributes", WORD),
            ("srWindow", SmallRect),
            ("dwMaximumWindowSize", Coord)]

    STD_INPUT_HADLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12

    stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)