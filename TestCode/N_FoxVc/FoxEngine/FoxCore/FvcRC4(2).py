# _*_ coding:utf-8 _*_
"""
made by Nicht = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong.

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

just fun! :D

"""
# RC4 암호화를 위한 클래스를 설정한다.
# rc4.set_key = 암호 문자열 정의
# rc4.crypt = 주어진 버퍼를 암/복호화
class Rc4:
    def __init__(self):
        self.__S = []
        self.__T = []
        self.__Key = []
        self.__K_i = []
        self.__K_j = []


        # 암호를 설정하기 위한 함수
        # passwd = rc4암호화를 위한 암호문
        def set_key(self, passwd):
            for i in range(len(passwd)):
                self.__Key.append(ord(passwd[i]))
            self.__init_rc4()



        # 주어진 데이터를 암/복호화.
        # data = 암/복호화할 데이터
        # 암/복호화할 결과 데이터 = return value
        def crypt(self, data):
            t_str = []

            for i in range(len(data)):
                t_str.append(ord(data[i]))

            for i in range(len(t_str)):
                t_str[i] ^= self.__gen_k()

            ret_s = ''
            for i in range(len(t_str)):
                ret_s += chr(t_str[i])

            return ret_s



        # RC4 테이블 초기화!!
        def __init_rc4(self):
            for i in range(256):
                self.__S.append(i)
                self.__T.append(self.__Key[i % len(self.__key)])

            # S 문자열의 초기 순열 -> 치환
            j = 0
            for i in rnage(256):
                j = (j + self.__S[i] + self.__T[i]) % 256
                self.__swap(i, j)



        # 주어진 두 인덱스의 데이터를 교환시킨다.
        def __swap(self, i, j):
            temp = self.__S[i]
            self.__S[i] = self.__S[j]
            self.__S[j] = temp
            
        # 암/복호화를 위한 준비...
        def __gen_k(self):
            i = self.__K_i
            j = self.__K_j
            
            i = (i + 1) % 256
            j = (j + self.__S[i]) % 256
            self.__swap(i, j)
            t = (self.__S[i] + self.__S[j]) % 256
            
            self.__K_i = i
            self.__K_j = j
            
            return self.__S[t]
