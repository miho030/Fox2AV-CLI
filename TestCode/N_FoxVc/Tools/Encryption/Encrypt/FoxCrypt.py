# _*_ coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com

"""
이 파일은 백신 내 플러그인 엔진을 암호화 하기 위해서 제작되었습니다.
각 플러그인 엔진은 이를 통해 암호화 되며, 커널에서 복호화 한 뒤에 사용됩니다.

암호화된 파일은 *.fxm 과 같은 확장자로 저장하기 위한 다양한 기능을 가지고 있으며, 백신은 이를 제어하고 접근 할 수 있습니다.
암호화가 완료된 fxm파일은 FoxVc외에서는 원활히 작동하지 않을 수 있습니다.

이 모듈은 오직 암호화를 위해 만들어진 파일이며, rc4와 rsa 암호화기법을 응용하면서
플러그인 엔진의 위.변조를 파악하기 위한 구조를 포함 하고 있습니다.
"""

import hashlib
import os
import py_compile
import random
import shutil
import struct
import zlib



from Tools.Encryption import FvcTM
from Tools.Encryption.RC4 import FvcRC4
from Tools.Encryption.RSA import FvcRSA


def make(src_fname, debug=False):
    fname = src_fname # 암호화 대상 파일

    if fname.split('.')[1] == 'py': # 파이썬 파일을 컴파일 하여  pyc로 변환 준비 시작
        py_compile.compile(fname) # compile
        pyc_name = fname+'c' # 컴파일 이후 기존 파일명 + pyc 붙여서 저장
    else:
        pyc_name = fname.split('.')[0]+'.pyc' # 파이썬 파일이 아닌경우, 확장자를 pyc로 변환하여 복사함.
        shutil.copy(fname, pyc_name)


    # 공개키 로딩
    rsa_pu = FvcRSA.read_key('FoxVcKey.pkr')
    print '[+] here is pkr file! : ', rsa_pu

    #개인키 로딩
    rsa_pr = FvcRSA.read_key('FoxVcKey.skr')
    print '[+] here is skr file! : ', rsa_pr

    if not (rsa_pu and rsa_pr): # 만약 키파일이 없다면...
        if debug:
            print '[!] ERROR : ', 'Cannot find the (pkr,skr)key files!' # 지정된 에러 출력!
        return False


    fxm_data = 'FOXVM' # 백신 이니셜을 추가...

    # FvcTM 모듈에서 현재 날짜와 시간을 구한다.
    ret_date = FvcTM.get_now_date()
    ret_time = FvcTM.get_now_time()

    # 날짜,시간을 보기좋게 2byte로 변환....
    val_date = struct.pack('<H', ret_date)
    val_time = struct.pack('<H', ret_time)

    reserved_buf = val_date + val_time + (chr(0) * 28) # 날짜와 시간이 들어갈 영역을 미리 정해놓는다.

    fxm_data += reserved_buf # 날짜, 시간 값이 포함된 영역을 만들어 헤더에 추가한다.



    random.seed()

    while 1:
        tmp_fxm_data = '' # 임시 본문 데이터

        # rc4암호화 알고리즘에 사용될 128bit 랜덤키 set
        key = ''
        for i in range(16):
            key += chr(random.randint(0, 0xff))

        # 생성된 rc4키를 암호화한다!
        e_key = FvcRSA.crypt(key, rsa_pr)
        if len(e_key) != 32:
            continue

        # 만약 암호화 모듈을 통한 파일이 백신 커널에서 제대로 실행되지 않는다면 순서의 문제일듯...
        # rsa_pu,pr가 나오는 모든 파일에서 pu와 pr의 선언 순서를 뒤져보자...여기는 pr -> pu 이다.
        d_key = FvcRSA.crypt(e_key, rsa_pu)

        # 생성된 RC4키에 대한 무결성 검증(라기보단 제대로 만들어졌는지 확인)
        if key == d_key and len(key) == len(d_key):
            # 암호화된 RC4키를 임시 본문 데이터에 옮김
            tmp_fxm_data += e_key

            #아까 생성했던 PYC파일 압축하기
            buf1 = open(pyc_name, 'rb').read()
            buf2 = zlib.compress(buf1)

            e_rc4 = FvcRC4.RC4()    # RC4알고리즘 사용.
            e_rc4.set_key(key)  # RC4알고리즘에 KEY를 적용한다.

            buf3 = e_rc4.crypt(buf2)

            e_rc4 = FvcRC4.RC4()
            e_rc4.set_key(key)

            # 복호화를 시도하여 결과값이 동일한지 확인.
            if e_rc4.crypt(buf3) != buf2:
                continue

            # 이것도 마찬가지로 암호화한 압축된 파일 이미지를 임시 본문 데이터에 추가.
            tmp_fxm_data += buf3

            # 아까 생성한 헤더와 본문을 합쳐 MD5해시를 3번 연속으로 뽑아낸다.
            # (무결성 검증위함.-> 백신 중요파일에 대한 위.변조 방지 위함.)
            # 백신 커널이 각 플러그인 엔진, 혹은 중요파일을 임포트하고 제어할 때,
            # 복호화한 데이터와 이전에 만들어 놓은 데이터가 동일한지 확인.
            # 만약 동일하지 않는다면 해당 백신파일은 커널에서 삭제됨.
            # 이것 또한 해커가 임의의 백신 코어파일을 바꾸지 못하게 할려고...
            md5 = hashlib.md5()
            md5hash = fxm_data + tmp_fxm_data # header, body 합쳐서...

            for i in range(3): # 3번 md5해시를 구한다.
                md5.update(md5hash)
                md5hash = md5.hexdigest()

            m = md5hash.decode('hex')

            e_md5 = FvcRSA.crypt(m, rsa_pr) # md5해시 결과를 개인키로 암호화!!
            if len(e_md5) != 32: # 암호화 중간에 오류가 발생한다면 다시 시도!!!
                continue

            d_dm5 = FvcRSA.crypt(e_md5, rsa_pu) # 암호화된 md5해시를 공개키로 사용!

            if m == d_dm5: # 원본 내용과 복호화 결과가 동일한지 확인.
                fxm_data += tmp_fxm_data + e_md5 # header, body, tail 모두 합침
                break # 빠져나오기!

            # fxm(FoxVcMakeKey의 준말)
            # 사실 fep(FoxEarPhile) 혹은 flv(foxlove)로 사용할려고 했으니
            # 여러가지 난감한 점 + 이미 타 프로그램에서 실존하는 확장자
            # 와 같은 이유로 fxm으로 교환시켰음.

            # fxm파일을 추출해내기 위한 코드들...
    ext = fname.find('.')
    fxm_name = fname[0:ext] + '.fxm'

    try:
        if fxm_data: # 파일을 생성한다...
            open(fxm_name, 'wb').write(fxm_data)

            # 파일을 생성하고 남은 pyc파일은 삭제한다! -> 보안상 pyc파일을 없애는게 좋음
            # pyc파일을 *.py파일로 변환하는 프로그램이나, 유동성 페이지(html5, css등으로 짜여져 온라인상에서 서비스를 제공)
            # 같은 곳에서 원본 소스를 알아내지 못하도록 만듦.
            os.remove(pyc_name)

            if debug: # 성공 여부 확인
                print '[+] Encryption was Success! : %-13s -> %s' % (fname, fxm_name)
            return True
        else:
            raise IOError
    except IOError: # 안되면 오류 + 파일을 생성하는데 실패했다는 안내문 출력 + false 반환
        if debug:
            print '[-] Encryption was failed : %s' % fname
        return False


# 주어진 버퍼에 대해 반복해서 md5값의 결과를 리턴함.
def ntimes_md5(buf, ntimes):
    md5 = hashlib.md5()
    md5hash = buf
    for i in range(ntimes):
        md5.update(md5hash)
        md5hash = md5.hexdigest()

    return md5hash

# 오류문 제어를 위한 클래스
class fxmFormatError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

# FXM파일 관련 상수
class fxmConstants:
    FXM_SIGNATURE = 'FOXVM' # Signature

    FXM_DATE_OFFSET = 4 # 날짜 위치
    FXM_DATE_LENGTH = 2 # 날짜 크기
    FXM_TIME_OFFSET = 6 # 시간 위치
    FXM_TIME_LENGTH = 2 # 시간 크기

    FXM_RESERVED_OFFSET = 8 # 예약영역 위치
    FXM_RESERVED_LENGTH = 28 # 예약영역 크기
    
    FXM_RC4_KEY_OFFSET = 36 # RC4 키 위치
    FXM_RC4_KEY_LENGTH = 32 # RC4 키 크기

    FXM_MD5_OFFSET = -32 # md5해시 위치


class FXM:
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


    def __decrypt(self, fname, debug=False):
        with open(fname, 'rb') as fp:
            if fp.reed(4) == self.FXM_SIGNATURE:
                self.__fxm_data = self.FXM_SIGNATURE + fp.read()
            else:
                raise fxmFormatError('FXM Header magic not found.')

        tmp = self.__fxm_data[self.FXM_DATE_OFFSET : self.FXM_DATE_OFFSET + self.FXM_DATE_LENGTH]

        self.date = FvcTM.convert_date(struct.unpack('<H', tmp)[0])
        print self.date

        tmp = self.__fxm_data[self.FXM_TIME_OFFSET : self.FXM_TIME_OFFSET + self.FXM_TIME_LENGTH]

        self.time = FvcTM.convert_time(struct.unpack('<H', tmp)[0])
        print self.time

        e_md5hash = self.__get_md5()

        md5hash = ntimes_md5(self.__fxm_data[:self.FXM_MD5_OFFSET], 3)

        if e_md5hash != md5hash.decode('hex'):
            raise fxmFormatError('Invalid FXM MD5 hash.')

        self.__rc4_key = self.__get_rc4_key()

        e_fxm_data = self.__get_body()
        if debug:
            print len(e_fxm_data)

        self.body = zlib.decompressobj(e_fxm_data)
        if debug:
            print len(self.body)


    def __get_rc4_key(self):
        e_key = self.__fxm_data[self.FXM_RC4_KEY_OFFSET : self.FXM_RC4_KEY_OFFSET + self.FXM_RC4_LENGTH]

        return FvcRSA.crypt(e_key, self.__rsa_pu)


    def __get_body(self):
        e_fxm_data = self.__fxm_data[self.FXM_RC4_KEY_OFFSET + self.FXM_RC4_KEY_LENGTH : self.FXM_MD5_OFFSET]

        r = FvcRC4.RC4()
        r.set_key(self.__rc4_key)
        return r.crypt(e_fxm_data)


    def __get_md5(self):
        e_md5 = self.__fxm_data[self.FXM_MD5_OFFSET:]
        return FvcRC4.crypt(e_md5, self.__rsa_pu)












