# _*_ coding:utf-8: _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com

import os
import hashlib

class FoxMain:
    # 플러그인 엔진을 초기화함
    def FreshPlugEnG(selfself, plugins_path):
        return 0

    # 플러그인 엔진을 종료함
    def DownPlugEng(self):
        return 0

    # 악성코드 검사 모듈
    def Scan(self, filehandle, filename):
        try:
            mm = filehandle

            size = os.path.getsize(filename)
            if size == 68:
                m = hashlib.md5()
                m.update(mm[:68])
                fmd5 = m.hexdigest()

                if fmd5 == '44d88612fea8a8f36de82e1278abb02f':
                    return True, 'Eicar-Test-File (Not a virus)', 0
        except IOError:
            pass
        # 만약 악성코드를 발견하지 못한다면...
        return False, '', -1

    def CureInfected(self, filename, malware_ID):
        try:
            if malware_ID == 0:
                os.remove(filename)
                return True
        except IOError:
            pass
        return False

    def VirusList(self):
        vlist = list()
        vlist.append('Eicar-Test-File (Not a virus)')

        return vlist

    def GetInfoPlugEng(self):
        info = dict()


        info['author'] = 'Nicht; Lee Joon Sung'
        info['version'] = '1.0'
        info['title'] = 'Eicar Scan Engine'
        info['fxm_name'] = 'eicar'

        return info
