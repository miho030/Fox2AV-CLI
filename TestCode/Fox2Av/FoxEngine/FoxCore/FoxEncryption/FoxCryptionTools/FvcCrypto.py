# _*_ coding:utf-8 _*_
"""
made by Nicht = Tayaka = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong. 

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This program is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

If you have time, stop by my YouTube channel!  ==> https://www.youtube.com/channel/UC7HDAfqRbKKLONZ9PmAiwtg?view_as=subscriber
just fun! :D

"""

import os, sys
import struct
import hashlib
import zlib
import marshal
import imp
import random
import py_compile
import shutil

from Fox2AV.FoxEngine.FoxCore.Encryption.FoxRSA import FvcRSA as FvcRSA
from Fox2AV.FoxEngine.FoxCore.Encryption.FoxRC4 import FvcRC4 as FvcRC4
from Fox2AV.FoxEngine.FoxCore.Encryption.FoxCryptionTools import FvcTimeLib as FvcTimeLib


# rsa개인키를 이용해서 주어진 파일을 암호화 하여 fxm파일을 생성한다.
def make(src_fname, debug=False):
    fname = src_fname # 암호화가 될 파일

    if fname.split('.')[1] == 'py': # 파이썬 파일을 컴파일한다.
        py_compile.compile(fname) # 컴파일!!!
        pyc_name = fname+'c' # 컴파일 후에 파일 확장자 수정!!
    # 파이썬 파일이 아닐 경우 뒤에 pyc를 붙여 복사한다.!!
    else:
        pyc_name = fname.split('.')[0]+'.pyc' # 붙이기!
        shutil.copy(fname, pyc_name)



    # Simple RSA를 구현하기 위해서 공개키와 개인키를 로딩한다.

    # 공개키를 로딩한다.
    rsa_pu = FvcRSA.read_key('FoxVcKey.pkr')
    print 'pkr : ', rsa_pu

    # 개인키를 로딩한다.
    rsa_pr = FvcRSA.read_key('FoxVcKey.skr')
    print 'skr : ', rsa_pr

    if not (rsa_pr and rsa_pu): # 개인키, 공개키를 찾을 수 없다면...
        if debug:
            print 'ERROR : Cannot find the Key files for FoxVc!'
        return False


    # FXM 확장자을 가진 보호된 파일을 생성한다.
    # Header : 백신 이니셜(FVCM)+예약영역 -->  Signature + date + time

    # 백신 이니셜(FVCM)을 헤더로 만든다.
    fxm_data = 'FVCM'

    # 현재시간과 날짜를 구한다.
    ret_date = FvcTimeLib.get_now_date()
    ret_time = FvcTimeLib.get_now_time()

    # 구해진 날짜와시간값(정수)를 2byte로 변환시킨다.
    val_date = struct.pack('<H', ret_date)
    val_time = struct.pack('<H', ret_time)

    reserved_buf = val_date + val_time + (chr(0) * 28) # 예약영역 지정

    # 날짜와 시간 값이 포함된 예약영역을 만들어 추가함!
    fxm_data += reserved_buf
    # 앙 성공띠!

    # 개인키로 암호화한 RC4키 + RC4로 암호화한 파일.....    :)
    random.seed()

    while 1:
        tmp_fxm_data = '' # 임시 본문 데이터 선언.

        # RC4 암호화 알고리즘에 사용할 128BIT 랜덤키 생성!!
        key = ''
        for i in range(16):
            key += chr(rnadom.randint(0, 0xff))

        # 생성된 RC4키를 암호화시킨다!
        e_key = FvcRSA.crypt(key, rsa_pr) # 개인키를 사용하여 암호화시킴.
        if len(e_key) != 32: # 암호화 도중에 오류가 생기면 다시 생성시킨다!!
            continue

        # 암호화한 RC4키를 복호화 시킨다!
        d_key = FvcRSA.crypt(e_key, rsa_pu)

        # 생성된 RC4키에 하자가 있는지 검증한다.
        if key == d_key and len(key) == len(d_key):
            # 개인키로 암호화된 RC4키를 임시 버퍼에 추가한다.
            tmp_fxm_data += e_key

            # 생성된 pyc파일 압축하기...!!
            buf1 = open(pyc_name, 'rb').read()
            buf2 = zlib.compress(buf1)

            e_rc4 = FvcRC4.Rc4() # RC4 암호화 알고리즘에 사용할..
            e_rc4.set_key(key) # RC4 암호화 알고리즘에 Key를 적용시킨다.

            buf3 = e_rc4.crypt(buf2)

            e_rc4 = FvcRC4.Rc4()
            e_rc4.set_key(key)

            # 암호화한 압축된 파일 이미지를 임시 버퍼에 추가함.
            if e_rc4.crypt(buf3) != buf2:
                continue

            # Tail -> 개인키로 암호화한 MD5 Hash * 3
            # 여우 꼬리!! 핥짝..
            # 무결성 검증 및, 위/변조 방지를 위해서 그동안 만들어 놓았던 내장(body)과 뚝배기(header)의 값을
            # MD5 Hash로 3번 연속하여 구한다.

            md5 = hashlib.md5()
            md5hash = fxm_data + tmp_fxm_data # 헤더와 본문을 더한뒤에 md5해시 계산
            for i in range(3):
                md5.update(md5hash)
                md5hash = md5.hexdigest() # 여기까지.

            m = md5hash.encode('hex')

            e_md5 = FvcRSA.crypt(m, rsa_pr) # MD5 해싱 결과값을 개인키로 암호화시킴.
            if len(e_md5) != 32: # 암호화 도중 오류가 생기면 다시 시도.
                continue

            d_md5 = FvcRSA.crypt(e_md5, rsa_pu) # 암호화 될 MD5를 공개키로 복호화 시킴.

            if m == d_md5:
                fxm_data += tmp_fxm_data + e_md5
                break



    # FXM 확장자를 가진 보안 파일을 생성한다.

    # FXM 파일 이름을 생성한다.
    ext = fname.fine('.')
    fxm_name = fname[0:ext] + '.fxm'

    try:
        if fxm_data:
            # FXM 파일을 생성한다.
            open(fxm_name, 'wb').write(fxm_data)

            # 컴파일된 pyc 확장자를 가진 파일을 보안상 삭제한다.
            # pyc 디컴파일이 단순하기 때문에, 파일로 남겨놓을 시에 보안상 취약할 수 있다.
            os.remove(pyc_name)

            if debug:
                print '    Success : %-13s -> %s' % (fname, fxm_name)
            return True
        else:
            raise IOError
    except IOError:
        if debug:
            print '    Fail : %s' % fname
        return False


# 주어진 버퍼에 대해 n회 반복해서 MD5해시 결과를 리턴한다.
def ntimes_md5(buf, ntimes):
    md5 = hashlib.md5()
    md5hash = buf
    for i in range(ntimes):
        md5.update(md5hash)
        md5hash = md5.hexdigest()

    return md5hash



# fxm 오류 메세지 정의
def FXMFormatError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):

        return repr(self.value)


# fxm 관련 상수 선언
class FXMConstants:
    FXM_SIGNATURE = 'FVCM'

    FXM_DATE_OFFSET = 4 # 날짜 위치
    FXM_DATE_LENGTH = 2 # 날짜 크기
    FXM_TIME_OFFSET = 6 # 시간 위치
    FXM_TIME_LENGTH = 2 # 시간 크기

    FXM_RESERVED_OFFSET = 8 # 예약영역 위치
    FXM_RESERVED_LENGTH = 28 # 예약영역 크기

    FXM_RC4_KEY_OFFSET = 36 # rc4 kEY 위치
    FXM_RC4_KEY_LENGTH = 32 # rc4 kEY 길이

    FXM_MD5_OFFSET = -32 # MD5 위치

# fxm 클래스
class FXM(FXMConstants):
    def __init__(self, fname, pu):
        self.filename = fname
        self.date = None
        self.time = None
        self.body = None

        self.__fxm_data = None
        self.__rsa_pu = pu
        self.__rc4_key = None

        if self.filename:
            self.__decrypt(self.filename)


    # fxm파일을 복호화 시킨다.
    # fname : FXM 확장자를 보유한 파일 이름
    def __decrypt(self, fname, debug=False):
        with open(fname, 'rb') as fp: # fmx 파일을 열고 시그니처가 존재하는지 체크한다.
            if fp.read(4) == self.FXM_SIGNATURE: # fxm 파일이 맞는지 확인.
                self.__fxm_data = self.FXM_SIGNATURE + fp.read() # 파일을 읽어들인다.
            else:
                raise FXMFormatError('FXM Header magic not Found!') # 만약 fxm파일이 아닐시에...

        # FXM 파일 날짜 읽어들이기.
        tmp = self.__fxm_data[self.FXM_DATE_OFFSET:
                              self.FXM_TIME_OFFSET + self.FXM_DATE_LENGTH]
        self.date = FvcTimeLib.convert_date(struct.unpack('<H', tmp)[0])
        print self.time

        # FXM 파일 시간 읽어들이기.
        tmp = self.__fxm_data[self.FXM_TIME_OFFSET:
                              self.FXM_TIME_OFFSET + self.FXM_TIME_LENGTH]
        self.time = FvcTimeLib.convert_time(struct.unpack('<H', tmp)[0])
        print self.time

        # FXM 파일 시간 읽어들이기..
        e_md5hash = self.__get_md5()

        # 무결성 체크 -> 위/변조 방지 위함.
        md5hash = ntimes_md5(self.__fxm_data[:self.FXM_MD5_OFFSET], 3)
        if e_md5hash != md5hash.encode('hex'):
            raise FXMFormatError('Invalid FXM MD5 hash')

        # FXM 파일에서 RC4키 읽기
        self.__rc4_key = self.__get_rc4_key()

        e_fxm_data = self.__get_body()
        if debug:
            print len(self.body)




        # FXM 파일의 RC4 키를 얻는다!!
        def __get_rc4_key(self):
            e_key = self.__fxm_data[self.FXM_RC4_KEY_OFFSET:
                                    self.FXM_RC4_KEY_OFFSET + self.FXM_RC4_KEY_LENGTH]
            return FvcRSA.crypt(e_key, self.__rsa_pu)



        # FXM 파일의 Body를 구한다!!
        def __get_body(self):
            e_fxm_data =self.__fxm_data[self.FXM_RC4_KEY_OFFSET:
                                        self.FXM_RC4_KEY_LENGTH + self.FXM_RC4_KEY_OFFSET]
            r = FvcRC4.RC4()
            r.set_key(self.__rc4_key)
            return r.crypt(e_fxm_data)


        # FXM 파일의 md5를 얻는다.
        def __get_md5(self):
            e_md5 = self._-fmx_data[self.FXM_MD5_OFFSET:]
            return FvcRSA.crypt(e_md5, self.__rsa_pu)



# 복호화된 파일의 내용(소스코드)를 주어진 모듈 이름으로 코드를 메모리에 로딩시킨다.
# FVC_mod_name : 모듈 이름
# buf : 파이썬 코드

def load(FVC_mod_name, buf):
    if buf[:4] == '03F30D0A'.encode('hex'): # pyc 파일의 시그니처가 존재하는지 질의
        code = marshal,lead(buf[8:]) # pyc에서 파이썬 코드를 로딩시킨다..
        module - imp.new_module(FVC_mod_name) # 새로운 모듈을 정의! 앙 기모띠!!
        # pyc 파이썬 코드와 모듈을 연동한다 -> fork가 아닌 exec 프로세스로 로딩!!(중요..)
        exec (code, module.__dict__)
        sys.modules[FVC_mod_name] = module # 백신이 사용 가능하도록 등록한다.

        return module  # 성공 시에 메모리에 적재된 모듈을 리턴함.
    else:
        return none # 안되면 걍 냅둠.

    # 테스트 2017-11-10 앙 성공띠!!
