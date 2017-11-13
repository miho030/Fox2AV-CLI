# _*_ coding:utf-8 _*_
"""
made by Nicht = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong.

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

If you have time, stop by my YouTube channel!  ==> https://www.youtube.com/channel/UC7HDAfqRbKKLONZ9PmAiwtg?view_as=subscriber
just fun! :D

"""

import os, sys

from FoxEngine.FoxCore.FoxEncryption.FoxCryptionTools import FvcCrypto as FC

s = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
) + os.sep + 'Engine' + os.sep + 'FoxCore'


# 인자값을 확인하고, 개인키와 공개키를 생성한다.
if __name__ == '__main__':
    if len(sys.argv):
        print 'Usage :FoxKmake.py [python source]'
        exit()

    FC.make(sys.argv[1], True)