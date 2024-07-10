# -*- coding: utf-8 -*-

# Author : github.com/miho030

# 이 파일은 단순히 새로운 소스코드를 실험하고, 보완하기 위해 생성됨
# 필요 라이브러리 임포트
import sys

# 트러블 슈팅을 위한 리스트

"""

1. sys.version의 구현과 인덱신
2. sys.version으로의 한계(?)
3. sys.version과 sys.version_info의 장단점과 스크립트상 용이점
4. sys모듈을 사용하여 스크립트를 2.x와 3.x에서 호환성 스크립트를 개발하지 않고 다른 방법으로..
5. 호환성 관련하여 타 모듕 임포트 시의 문제

"""

# sys.version의 구축
sys.version

a=sys.version # 변수로 사용가능

# 인덱싱 구현

# 2버전인지 3버전인지 확인
print a[:1]  # 예 -> 2 3

# or
print a[:3]  # 예 -> 2.7 3.4 3.6

# 2,x인지 3.x인지 구분하는 함수의 구축
# 일단 편의상 Pyver2와 Pyver3의 함수를 print문으로 구축함.

def Pyver2():
    print "This Function is Python 2.x version Optimization module!"

def Pyver3():
    print ( "This Function is Python 2.x version Optimization module!" )


PyVer=sys.version

if PyVer[:1] == 2:
    print "[!] ", "You have Python 2!\n", "[+] ", "Start python2 modules..."
    Pyver2()
else:
    if PyVer[:1] ==3:
        print ( "You" )
        Pyver3()
    else:
        print ( "You dont have python!" )


# 코드가 완벽해 보이지만 실제로 파이참에서 실행시켜보면 설계대로 구동되지 않았다..
# 첫번째 if와 두번째 if도 뛰어넘고 마지막 else문을 출력하였다. --> 아마 버전 출력해서 비교하는 부분에 문제가 있는듯..
# 애초에 문법적으로 안틀리고 제대로 구축한건가? ㅋㅋㅋㅋㅋㅋ

# 새로운 코드! sys.version_info의 major변수를 사용해서 구축해봄 ㅇㅇ
# 일단 전제와 같이할거임

Pyverver=sys.version_info

if not sys.version_info[:1] == (2,):
    print "[ + Error + ] ", "Python 2.x is not installed in your system !"
else:
    print "[+] ", "You have Python2.x!", "Start python 2.x modules...\n"
    Pyver2()
    pass

if sys.version_info[:1] == 3:
    print ("[+] ", "You have Python3.x!", "Start python 3.x modules..\n")
    Pyver3()
else:
    print "yo dont have python dude!"

"""
퍼킹 예! 제대로 실행된다.
"""



