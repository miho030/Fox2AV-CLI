# Author : github.com/miho030
# Kei_Choi교수님의 오픈소스 키콤백신을 참고

import os
import datetime
import types
import struct

#===========================================================================
#엔진 오류 출력문
#===========================================================================

class EngineError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Engine:
    def __init__(self, debug=False):
        self.debug = debug # 디버깅 여부를 판단

        self.plugin_path = None
        self.Foxfile = [] # 우선순위가 기록된 리스트
        self.Fox_modules = [] # 메모리에 로딩될 모듈

        self.max_datetime = datetime.datetime(2017, 6, 29, 0, 0, 0, 0)
        # 엔진의 가장 최신 시간 값을 지정
        # 초기 값은 2017년 06월 29일로 지정함.

        #백신이 만든 임시파일 모두 제거.
        self.__remove_Fox_temFile()


    def __remove_Fox_tempFile(self):
        tpath = tempFile.gettempdir()
        fl = glob.glob(tpath + os.sep + 'Foxtmp*')
        for name in fl:
            if os.path.isfile(name):
                try:
                    os.remove(name)
                except IOError:
                    pass
