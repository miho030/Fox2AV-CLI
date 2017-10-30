# _*_coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com


"""
이 파일은 RSA 암호화 기법을 사용해서 FoxVc의 플러그인과 악성코드 패턴을 암호화하는 목적으로 쓰이는 모듈입니다.
이 파일은 단순 암호화 및, 백신 보안 유지를 위해 제작되었습니다.

    설계한 암호화 기법은....

        1. Header : 백신 이니셜 + 정보 표시[lastest updated files](날짜, 시간값)
        2. Body : individual Key를 이용해 암호화된 RC4키 + RC4로 암호화된 압축된 내부 소스코드
        3. Tailer : 개인키로 암호화한 Header와 Body전체에 대해 md5를 3번 연산한 결과.


    이 복잡한 암호화 기법의 제작 기준은...

        1. 공격자가 복호화 키를 알아내어 임의로 암호화를 수행할 수 없도록 만들어야 한다.
        2. 암호화, 복호화 속도가 느리지 않고 빠른 속도로 실행되어야 한다.

    백신에 암호화 모듈을 적용한 이유.... :

        1. 카스퍼스키 백신이 크래커에 의해 백신 커널의 소스코드가 밝혀진 적이 있었다.
        2. 해커는 당연히 커널의 구조를 파악하고 이해하였으며,
        3. 백신 커널의 구조를 통해 자신의 커스텀 백신 엔진을 만들었다.
        4. 당연히 해커는 이를 카스퍼스키 정품에 넣어 배포하였고,
        5. 카스퍼스키 연구소는 이를 알아채지 못했다는 사건이 있었다.

    이러한 전모로, 당연히 소스코드가 나와 있는 필자의 백신(FoxVc)에는 의미가 없지만,
    만약에 필자의 백신을 커스텀하여 사용할 시스템 관리자에게는 당연히 필요한 모듈이라 생각하여 제작하게 되었음.

"""

import sys

import FvcRSA

if __name__ == '__main__':
    pu_fname = 'FoxVcKey.pkr'
    pr_fname = 'FoxVcKey.skr'

    if len(sys.argv) == 3:
        pu_fname = sys.argv[1]
        pr_fname = sys.argv[2]
    elif len(sys.argv) != 1:
        print 'Usage : FoxMrsaK.py [[PU filename] [PR filename]]'
        sys.exit(0)

    FvcRSA.create_key(pu_fname, pr_fname, True)

