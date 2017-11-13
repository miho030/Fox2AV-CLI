# _*_ coding:utf-8 _*_
"""
made by Nicht = tayaka = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong.

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

If you have time, stop by my YouTube channel!  ==> https://www.youtube.com/channel/UC7HDAfqRbKKLONZ9PmAiwtg?view_as=subscriber
just fun! :D

"""


# 악성코드 상태값
NOT_FOUND = 0 # 악성코드를 찾지 못함.
INFECTED = 1 # 악성코드에 감염됨.
SUSPECT = 2 # 악성코드 감염 의심
WARNING = 3 # 경고
ERROR = 88 # 에러 메세지 처리

MASTER_IGNORE = 0 # 현재 지원하지 않는 상태임. -> 파일 방치 처리
MASTER_PACK = 1 # 최상위 파일 재구성 압축함수(FoxMkArc) 처리 기능.
MASTER_DELELTE= 2 # 최상위 파일을 지울것.

ARCHIVE_ENGINE = 80 # 압축 해제 엔진

class FoxMain:
    # Reset the plugin engine.
    def FreshPlugEnG(self, plugins_path, vervose=False): 
        return 0
        
        
        
    # Halt the plugin engine.
    def DownPlugEnG(self):
        return 0
         
    # 커널 정보 출력 위해 개발된 함수.
    def GeInfoPlugEnG(self):
        info = dict()
        
        info['author'] = 'Nicht' # 제작자
        info['version'] = '1.0'
        info['title'] = 'Fox2Av Kenel'
        info['fxm_name'] = 'FoxKenel'
            
        return info