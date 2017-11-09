# _*_ coding:utf-8 _*_
"""
made by Nicht = tayaka = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong.

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

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

import FvcRSA
import FvcRC4
import FvcTimeLib


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
                    md5hash = md5.hexdigest()

                m = md5hash.encode('hex')
