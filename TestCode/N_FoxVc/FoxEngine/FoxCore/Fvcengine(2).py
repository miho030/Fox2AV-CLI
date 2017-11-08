# _*_coding:utf-8 _*_
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
import imp
import StringIO
import datetime
import mmap
import types
import glob
import re
import tempfile
import struct
import zipfile

import FvcCrypto
import FvcRSA
import FvcRC4
import FvcConst
import FvcTimeLib
import Fvcfile


# Definite Engine Error Mes.
class EngineKnownError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# definite Engine Class
class Engine:
    def __init__(self, verbose=False): # 플러그인 엔진 초기화 => 플러그인 엔진의 무결성, 위/변조 방지 위한 검사.
        self.verbose = verbose # 디버깅 여부 확인

        self.plugins_path = None # 플러그인 경로 설정
        self.fxmFiles = []
        self.fxm_modules = []

        # 플러그인의 가장 최근의 시간 값을 저장.
        # 초기값은 1980-01-01이다.
        self.max_datetime = datetime.datetime(1980, 1, 1, 0, 0, 0, 0)

        # 백신이 구동되면서 만든 임시 파일을들 모두 제거한다.
        self.__remove_Fvc_Temfile()

    # 임시 파일 제거를 위한 함수...
    def __remove_Fvc_Temfile(self):
        tpath = tempfile.gettemdir()
        FI = glob.glob(tpath + os.sep + 'ftmp*') # ftmp라는 확장자를 지정.
        for name in FI: # FI(ftmp확장자를 보유한 파일)이 존재하는지 확인..
            if os.path.isfile(name): # 만약 파일이 발견 된다면?
                try:
                    os.remove(name) # 응 삭제~
                except IOError:
                    pass
                except WindowsError:
                    pass


    # 지정된 경로(plugins_path)내에서 플러그인 엔진을 로딩하기 위한 기초 설정을 마무리한다.
    def set_plugins(self, plugins_path):
        # 플러그인 경로 지정.
        self.plugins_path = plugins_path

        # 플러그인 엔진 로딩 시에 어떤 엔진을 먼저 로딩할지 우선 순위을 조사한다.
        # 이는 악성코드 진단/치료시에 빠른 대처를 위함.
        if FvcConst.FVCDEBUG:
            pu = None
            ret = self.__get__fxm__list(plugins_path  + os.sep + 'FoxVcList.lst', pu)
        else:
            # FvcRSA,FvcCrypt.에서 생성한 rsa 공개키와 개인키 중,
            # 공개키(FoxVcKey.pkr)을 백신 커널에 로딩한다.
            pu = FvcRSA.read_key(plugins_path + os.sep + 'FoxVcKey.pkr')
            if not pu:
                return False

            ret = self.__get_fxm_list(plugins_path + os.sep + 'FoxVcList.fxm', pu)

        if not ret: # 만약 암호화된 FoxVcList.fxm 파일이 없다면...
            return False

        if self.verbose:
            print '[*] FoxVcList.%s : ' % ('lst' if FvcConst.FVCDEBUG else 'fxm')
            print '   ', self.fxmFiles

        for fxm_name in self.fxmFiles:
            fxm_path = plugins_path + os.sep + fxm_name
            try:
                name = fxm_name.split('.')[0]
                if FvcConst.FVCDEBUG:
                    f = none
                    module = imp.load_source(name, fxm_path.rsplit('.')[0] + '.py')
                    try:
                        os.remove(fxm_pathrsplit('.')[0] + '.pyc')
                    except WindowsError:
                        pass
                else:
                    f = FvcCrypto.KMD(fxm_path, pu) # 모든 fxm파일을 복호화함 -> 암호화된 플러그인 엔진들을 모두 복호화시킴.
                    data = f.body
                    module = FvcCrypto.load(name, data)

                if module: # 플러그인들을 메모리에 로딩 성공했을 시에..
                    self.fxm_modules.append(module)
                    self.__get_list_fxm_build_time(f)
            except IOERrror:
                pass
            except FvcCrypto.FXMFormatError:
                pass