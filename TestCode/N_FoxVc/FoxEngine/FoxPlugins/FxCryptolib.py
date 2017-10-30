# _*_ coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com

import hashlib

# 주어진 데이터에 대해서 md5해시를 구함.
def md5(data):
    return hashlib.md5(data).hexdigest()

# 각 플러그인 엔진에서 공통적으로 쓰이는 필수 함수들을 적재함.
# init, uninit, getinfo가 이 예임.
class FoxMain:
    def init(self, plugins_path):
        return 0

    def uninit(self):
        return 0

    def getinfo(selfself):
        info = dict()

        info['author'] = 'Nicht; Lee Joon Sung'
        info['version'] = '1.0'
        info['title'] = 'Eicar Scan Engine'
        info['fxm_name'] = 'eicar'

        return info