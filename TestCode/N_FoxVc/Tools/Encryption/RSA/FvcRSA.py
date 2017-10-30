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

        1. 공격자가 복호화 키를 알아내어 임의로 암호화를 수행할 수 없도   록 만들어야 한다.
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

# 주요 라이브러리 임포트
import base64
import marshal
import random


# 기본적인 rsa암호화 계산법 이용.

"""
유클리드 호제법을 이용하여 am +bn = gcd(Greatest Common Divisor)의 해가되는
정수 a, b를 찾아낸다.
"""


def __ext_euclid(a, b):
    i = -1
    list_r = list()
    list_q = list()
    list_x = list()
    list_y = list()

    i += 1
    list_r.append(a)
    list_r.append(b)

    list_q.append(0)
    list_q.append(0)

    list_x.append(1)
    list_x.append(0)

    list_y.append(0)
    list_y.append(1)

    i = 2

    while 1:
        list_r.append(list_r[i - 2] % list_r[i - 1])
        list_q.append(list_r[i - 2] / list_r[i - 1])

        if list_r[i] == 0:
            d = list_r[i - 1]
            x = list_x[i - 1]
            y = list_y[i - 1]

            if x < 0:
                x += b
            if y < 0:
                y += b

            return d, x, y

        list_x.append(list_x[i - 2] - (list_q[i] * list_x[i - 1]))
        list_y.append(list_y[i - 2] - (list_q[i] * list_y[i - 1]))
        i += 1



def __mr(n):
    composite = 0
    inconclusive = 0

    def get_kq(num):
        sub_k = 0

        sub_t = num - 1
        b_t = bin(sub_t)

        for sub_i in range(len(b_t) - 1, -1, -1):
            if b_t[sub_i] == '0':
                sub_k += 1
            else:
                break
        sub_q = sub_t >> sub_k
        return sub_k, sub_q

    k, q = get_kq(n)
    if k == 0:
        return 0

    for i in range(10):
        a = int(random.uniform(2, n))
        if pow(a, q, n) == 1:
            inconclusive += 1
            continue

        t = 0
        for j in range(k):
            if pow(a, (2 * j * q), n) == n - 1:
                inconclusive += 1
                t = 1
        if t == 0:
            composite += 1

    if inconclusive >= 6:
        return 1



def __gen_number(gen_bit):
    random.seed()

    b = ''
    for i in range(gen_bit - 1):
        b += str(int(random.uniform(1, 10)) % 2)
    b += '1'

    return int(b, 2)


def __gen_prime(gen_bit):
    while 1:
        p = __gen_number(gen_bit)
        if __mr(p) == 1:
            return p


def __get_ed(n):
    while 1:
        t = int(random.uniform(2, 1000))
        d, x, y = __ext_euclid(t, n)
        if d == 1:
            return t, x


def __value_to_string(val):
    ret = ''
    for i in range(32):
        b = val & 0xff
        val >>= 8
        ret += chr(b)

        if val == 0:
            break
    return ret


def __string_to_value(buf):
    plantext_ord = 0
    for i in range(len(buf)):
        plantext_ord |= ord(buf[i]) << (i * 8)

    return plantext_ord


def create_key(pu_fname='FoxVcKey.prk', pr_fname='FoxVcKey.skr', debug=False):
    p = __gen_prime(128)
    q = __gen_prime(128)

    n = p * q
    qn = (p - 1) * (q - 1)

    e, d = __get_ed(qn)

    pu = [e, n]
    pr = [d, n]

    pu_data = base64.b64encode(marshal.dumps(pu))
    pr_data = base64.b64encode(marshal.dumps(pr))

    try:
        open(pu_fname, 'wt').write(pu_data)
        open(pr_fname, 'wt').write(pr_data)

    except IOError:
        print '[-] ERROR : Failed to make keys'
        return False

    if debug:
        print '[*] Make RSA keys for FoxVc : %s, %s' % (pu_fname, pu_fname)

    return True


def read_key(key_filename):
    try:
        with open(key_filename, 'rt') as fp:
            b = fp.read()
            s = base64.b64decode(b)
            key = marshal.loads(s)

        return key
    except IOError:
        return None


def crypt(buf, key):
    plantext_ord = __string_to_value(buf)

    val = pow(plantext_ord, key[0], key[1])

    return __value_to_string(val)




