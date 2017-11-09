# _*_ coding:utf-8 _*_
"""
made by Nicht = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong.

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

just fun! :D

"""

import os, sys
import struct
import hashlib
import zlib
import marshal
import imp
import random
import py_compile
import shutil

import FvcRSA
import FvcRC4
import FvcTimeLib

# rsa개인키를 이용해서 주어진 파일을 암호화 하여 fxm파일을 생성한다.
def make(src_fname, debug=False):
    fname = src_fname # 암호화가 될 파일

    if fname.split('.')[1] == 'py': # 파이썬 파일을 컴파일한다.
        py_compile.compile(fname) # 컴파일!!!
        pyc_name = fname+'c' # 컴파일 후에 파일 확장자 수정!!
    # 파이썬 파일이 아닐 경우 뒤에 pyc를 붙여 복사한다.!!
    else:
        pyc_name = fname.split('.')[0]+'.pyc' # 붙이기!
        shutil.copy(fname, pyc_name)

        # Simple RSA를 구현하기 위해서 공개키와 개인키를 로딩한다.
        rsa_pu = FvcRSA.read_key
