# _*_ coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com


# 이 파일은 각 암호화 모듈을 가져와 fxm파일을 생성해내는 모듈입니다.
# 각 파일들은 py -> pyc -> fxm으로 변환되는 형태를 가지며,
# rsa 모듈에서 언급한 방식대로 3중 암호화 단계를 거쳐 완성됩니다.

import os, sys
import FoxCrypt
from Tools.Encryption.RSA import FvcRSA

FvcRSA.create_key('FoxVcKey.pkr', 'FoxVcKey.skr')

ret = FoxCrypt.make('FxCryptolib.py')  # 파일 암호화


# 악성코드 패턴파일이나, 멀웨어DB, 또는 백신 플러그인 엔진에 사용될 소스코드 파일을 암호화하는
# 목적이지만 pyc파일로 컴파일하는 특성상
# 암호화가 잘 실행되어 복호화까지 실행되는가에 대해서 암복호화 실행.
# 단순 파일을 암호화 할경우(NON_COMPILED FILE!!), 복호화하게 되면 기본 내용을 확인할 수 있을터..
# 복호화 모듈은 아직 개발 & 안정화중...

"""
ret = FoxCrypt.make('TestCode.txt')  # 파일 암호화
if ret:
    pu = FvcRSA.read_key('FoxVcKey.pkr') # 파일 복호화를 위한 공개키 로딩...
    kf = FoxCrypt.KMD('TestCode.fxm', pu)# 테스트코드 읽기 및 복호화
    print kf.body # 복호화된 파일의 내용 출력
    
"""


