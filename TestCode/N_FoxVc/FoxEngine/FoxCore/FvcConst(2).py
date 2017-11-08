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

# 디버깅 여부 설정/확인
FVCDEBUG = False

"""
* 악성코드 치료를 지시하는 상수들..
* 이는 커널이 사용자에 명령 하에, 악성코드를 치료할 시에 보내는 scan함수를 보조함.
* 정확히는 scan 콜백 함수에서 리턴값을 사용하기 위해 제작.

1. 사용자(의 명령) -> 커널 -> 커널이 우선순위를 조사하고 플러그인엔진을 로딩 ->
2. 플러그인 엔진이 진단 -> 진단 결과를 리턴 -> 
3. 리턴된 결과를 바탕으로 tui, gui 등의 환경으로 사용자에게 알리고 명령 하달 후 처리

"""
Fvc_ACTION_IGNORE = 0
Fvc_ACTION_CURE = 1
Fvc_ACTION_DELETE = 2
Fvc_ACTION_QUIT = 3