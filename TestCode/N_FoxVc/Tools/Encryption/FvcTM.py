# _*_coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com

# 이 파일은 암호화된 파일(*.fxm)내에 날짜와 시간 값을 추가하기 위해서 제작된 파일입니다.


import time

# 년, 월, 일 찾기
def convert_date(t):
    y = ((t & 0xFE00) >> 9) + 1980
    m = (t & 0x01E0) >> 5
    d = (t & 0x001F)

    print '[+] now : ', '%04d-%02d-%02d' % (y, m, d)
    return y, m, d


# 시, 분, 초 찾기
def convert_time(t):
    h = (t & 0xF800) >> 11
    m = (t & 0x07E0) >> 5
    s = (t & 0x001F) * 2

    print '[+] imao! : ', '%02d:%02d:%02d' % (h, m, s)
    return h, m, s

# 현재 날짜를 2byte 형식으로 변환
def get_now_date(now=None):
    if not now:
        now = time.gmtime()

    t_y = now.tm_year - 2017
    t_y = (t_y << 9) & 0xFE00
    t_m = (now.tm_mon << 5) & 0x01E0
    t_d = now.tm_mday & 0x001F

    return (t_y | t_m | t_d) & 0xFFF


def get_now_time(now=None):
    if not now:
        now = time.gmtime()

    t_h = (now.tm_hour << 11) & 0xF800
    t_m = (now.tm_min << 5) & 0x07E0
    t_s = (now.tm_sec /2) & 0x001F

    return (t_h | t_m | t_s) & 0xFFFF
