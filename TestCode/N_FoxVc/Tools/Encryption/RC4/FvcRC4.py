# _*_ coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com


"""
RC4 암호화를 위한 소스코드

"""

class RC4:
    def __init__(self):
        self.__S = []
        self.__T = []
        self.__Key = []
        self.__K_i = 0
        self.__K_j = 0

    # 암호 설정...
    def set_key(self, password):
        for i in range(len(password)):
            self.__Key.append(ord(password[i]))
        self.__init_rc4()

    # 데이터 암.복호화
    def crypt(self, data):
        T_Str = []

        for i in range(len(data)):
            T_Str.append(ord(data[i]))

        for i in range(len(T_Str)):
            T_Str[i] ^= self.__gen_K()

        ret_S = ''
        for i in range(len(T_Str)):
            ret_S += chr(T_Str[i])

        return ret_S

    # rc4 테이블 초기화...
    def __init_rc4(self):
        for i in range(256):
            self.__S.append(i)
            self.__T.append(self.__Key[i % len(self.__Key)])

        j = 0
        for i in range(256):
            j = (j + self.__S[i] + self.__T[i]) % 256
            self.__Swap(i, j)

    # 데이터 교환!
    def __Swap(self, i, j):
        temp = self.__S[i]
        self.__S[i] = self.__S[j]
        self.__S[j] = temp

    # 암.복호화에 필요한 stream 생성.
    def __gen_K(self):
        i = self.__K_i
        j = self.__K_j

        i = (i + 1) % 256
        j = (j + self.__S[i]) % 256
        self.__Swap(i, j)
        t = (self.__S[i] + self.__S[j]) % 256

        self.__K_i = i
        self.__K_j = j

        return self.__S[t]
