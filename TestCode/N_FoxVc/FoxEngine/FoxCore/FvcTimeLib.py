# _*_ coding:utf-8 _*_

# 플러그인 엔진에 가장 최신 값을 적용하기 위한 모듈.
# 이 모듈의 최신 시간값을 rc4와 rsa암호화 기법을 합쳐 만든 fxm확장자 파일내에 적용시킨다.
# -> 무결성 검증...

import time



# 주어진 정수에서 날짜를 get!
def convert_date(t):
    y = ((t & 0xFE00) >> 9) + 1980 # 초기값이 1980이기 때문에..
    m = (t & 0x01E0) >> 5
    d = (t & 0x001F)

    print '%04d-%02d-%02d' % (y, m, d)

    return y, m, d

# 정수에서 시간을 GET!
def convert_time(t):
    h = (t & 0xF800) >> 11
    m = (t & 0x07E0) >> 5
    s = (t & 0x001F) * 2

    print '%02d:%02d:%02d' % (h, m, s)

    return h, m, s

# 현재 날짜를 2byte 값으로 변환한다

def get_now_date(now=None):
    if not now:
        now = time.gmtime()

    t_y = now.tm_year - 1980
    t_y = (t_y << 9) & 0xFE00
    t_m = (now.tm_mon << 5) & 0x01E0
    t_d = now.tm_mday & 0x001F

    return (t_y | t_m | t_d) & 0xFFF

# 현재 시간을 2byte값으로 변환핟다.
def get_now_time(now=None):
    if not now:
        now = time.gmtime()

    t_h = (now.tm_hour << 11) & 0xF800
    t_m = (now.tm_min << 5) & 0x07E0
    t_s = (now.tm_sec / 2) & 0x001F

    return (t_h | t_m | t_s) & 0xFFF