# _*_ coding:utf-8 _*_
"""
made by Nicht

This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

If you have time, stop by my YouTube channel!  ==> https://www.youtube.com/channel/UC7HDAfqRbKKLONZ9PmAiwtg?view_as=subscriber
just fun! :D

"""
import os

from FoxEngine.FoxCore import FoxKernel
from FoxEngine.FoxCore import FoxCryptoLib


# FvcEngine 클래스
class FoxMain:
    # Reset the plug Engine
    def init(self, plugins_path, verbose=False): # 플러그인 엔진 초기화 함수
        return 0 # 플러그인 엔진 초기화 성공!


    # Halt the plug Engine
    def uninit(self): # 플러그인 엔진 종료
        return 0 # 플러그인 엔진 종료 성공!


    # scan and analysis system. -> for checking malware
    def scan(self, filehandle, filename, fileformat, filename_ex): # 악성코드 검사 함수
        try:
            mm = filehandle # 커널이 열어놓은 파일을 mmap을 이용하여 exce로 메모리상에 로딩...

            size = os.path.getsize(filename) # 파일의 사이즈를 먼저 구한다.
            if size == 68: # 사이즈가 68바이트라면 굳이 md5해시를 구해서 악성코드 진단할 필요 없음. 하지만 제대로된 검증을 위해...
                # 권장되는 악성코드 검사는 특정 위치 진단법..
                fmd5 = FoxCryptoLib.md5(mm[:68])

                if fmd5 == '44d88612fea8a8f36de82e1278abb02f': # md5해시 매칭시에 악성코드로 분류.
                    return True, 'Eicar-Test-File (not a virus!)', 0, kernel.INFECTED # 커널에게 악성코드임을 통보함.
        except IOError:
            pass

        return False, '', -1, kernel.NOT_FOUND



    # 악성코드를 치료한다!
    def disinfect(self, filename, Malware_ID):
        try:
            if Malware_ID == 0:
                os.remove(filename)
                return True
        except IOError:
            pass

        return False



    #커널에 진단 가능한 악성코드의 리스트를 반환함 -> 소비자(사용자)가 백신의 기능을 적당히 파악하기 위해서.
    def listvirus(self):
        vlist = list()

        vlist.append('EOCAR-Test-FIle (not a virus)')

        return vlist

    # 플러그인 엔진의 주요 정보를 알려준다.
    def getinfo(self):
        info = dict()

        info['author'] = 'Nicht'
        info['version'] = '1.0'
        info['title'] = 'EICAR-Test-Engine' # 엔진 설명
        info['fxm_name'] = 'eicarMal' # 보호된 엔진파일 이름
        info['sig_num'] = 1 # 진단/치료 가능한 악성코드 갯수

        return info
