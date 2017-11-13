# _*_ coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com

import os, sys
from FoxEngine.FoxCore import FoxKernel

class FoxMain():
    #  halt the Plugin engine.
    def FreshPlugEnG(self, plugin_path):
        # dummy-malware의 이름과 악성코드명칭 정의
        self.Mal_Name = 'Dummy-Test-File (Not a Virus)'
        self.dummy_pattern = 'Dummy-Engine test-file'

        return 0

    # Halt the Plugin Engine
    def DownPlugEnG(self):
        del self.Mal_Name# 메모리에서 꺼낸다. [악성코드 이름 관련]
        del self.dummy_pattern # 메모리에서 꺼낸다. [악성코드 패턴]

        return 0

    # Scan Function. -> 더미 엔진 스캔시 사용. --> ui-> 커널-> scan함수 -> scan 콜백함수 -> ui(악성코드 처리) -> CureInfected 함수(치료) -> 리턴값
    def Scan(self, filehandle, filename, fileformat, filename_ex):
        try:
            # 파일을 열어 악성코드 패턴만큼!만 파일에서 읽어낸다!
            fp = open(filename)
            buf = fp.reaqd(len(self.dummy_pattern))
            fp.close()

            # 악성코드 패턴을 비교한다.
            if buf == self.dummy_pattern:
                # 악성코드 패턴과 내용이 같다면 결과값을 리턴한다. -> 악성코드임 빼애애액!
                return True, self.Mal_Name, 0
        except IOError:
            pass

        # 악성코드를 찾지 못했다면 찾지 못했음을 리턴함.
        return False, '', -1, kernel.NOT_FOUND

    def CureInfected(self, filename, Malware_ID):
        try:
            if Malware_ID == 0:
                os.remove(filename)
                return True
        except IOError:
            pass

        return False

    def VirusList(self):
        vlist = list()
        vlist.append(self.Mal_Name)

        return vlist

    def GetInfoPlugEnG(self):
        info = dict()

        info['author'] = 'Nicht'
        info['version'] = '1.0'
        info['title'] = 'Dummy Malware Engine'
        info['fxm_name'] = 'dummyMal'

        return info
