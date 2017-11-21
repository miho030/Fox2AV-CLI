# _*_ coding:utf-8: _*_
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

import zipfile
from FoxEngine.FoxCore import FoxKernel

class FoxMain:
    # 플러그인 엔진 초기화.
    def FreshPlugEnG(self, plugins_path, verbose=False):
        self.handle = {} # 압축파일 핸들링
        return 0 # 플러그인 엔진 초기화 성공시에.

    # 플러그인 엔진 종료.
    def DownPlugEnG(self):
        return 0 # 플러그인 엔진 종료 성공시에..

    # 플러그인 엔진의 주요 정보를 전송한다.
    def GetInfoPlugEnG(self):
        info = dict() # 플러그인 엔진의 정보는 사전형 변수!

        info['author'] = 'Nicht'
        info['version'] = '1.0'
        info['title'] = 'Fox Zip Archive Engine' # 엔진 설명
        info['fxm_name'] = 'Zip' # 보호된 엔진파일 이름
        info['engine_type'] = FoxKernel.ARCHIVE_ENGINE # 엔진 타입
        info['make_arc_type'] = FoxKernel.MASTER_PACK # zip archive 타입의 악성코드 치료 후, 재압축 유무

        return info
