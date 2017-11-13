# _*_ coding:utf-8 _*_
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

import hashlib
from ctypes import c_ushort

# 제공된 데이터에 대해서 md5 해시를 구한다.
def md5(data):
    return hashlib.md5(data).hexdigest()


class FoxMain:
    # 플러그인 엔진 초기화
    def FreshPlugEnG(self, plugins_path, verbose=False):
        return 0

    # 플러그인 엔진 종료
    def DownPlugEnG(self):
        return 0

    # 플러그인 엔진의 주요정보를 보내줌
    def GetInfoPlugEnG(self):
        info = dict() # 사전형 변수 선언

        info['author'] = 'Nicht' # 제작자
        info['version'] = '1.0' # 버전
        info['title'] = 'Crypto Library' # 엔진 설명
        info['fxm_name'] = 'FoxCryptoLib' # 엔진 파일 이름

        return info