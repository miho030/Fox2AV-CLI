# _*_ coding:utf-8: _*_
"""
made by Nicht = Lee joon sung,
South Korea. Seoul. Gangnam. gaepodong.

contact admin = miho0_0@naver.com OR anonymous0korea0@gmail.com(youtube) OR miho03092@gmail.com(gmail)
This is Opensource Computer Anti-Virus program.
anyone can modificate this script. n you can edit this program on own your system environment.

This AV is compiled by Pycharm-community, made with Python 2.7.12, licensing on GNU Gnu Public License Ver.3.

If you have time, stop by my YouTube channel!  ==> https://www.youtube.com/channel/UC7HDAfqRbKKLONZ9PmAiwtg?view_as=subscriber
just fun! :D

"""


# 편이상 주석문 미작성
# 주석문 작성은 향후에 진행할 예정..
# 2017-12-10 기준 주석문 작성 완료.


import os
import re
import struct
import glob
import marshal
import time
import math


# 메세지 출력함수..
def vprint(header, section=None, msg=None):
    if header:
        print '[*] %s' % header

    if section:
        if len(msg) > 50:
            new_msg = msg[:22] + ' ... ' + msg[-22:]
        else:
            mew_msg = msg
        print '    [-] %-20s: %s' % (section, new_msg)


# 악성코드 패턴 인스턴스
handle_pattern_md5 = None # 악성코드 패턴 핸들링(MD5 Hash)


# 파일 분석을 위한 JSON 정규표현식 컴파일
p_text = re.compile(r'[\w\s!"#$%&\'()*+,\-./:;<=>?@\[\\\]\^_`{\|}~]')
p_md5_pattern_ext = re.compile(r'\.s(\d\d)$', re.IGNORECASE)



# 악성코드 패턴을 초기화 시킨다.
class PatternMD5:
    def __init__(self, plugins_path):
        self.sig_sizes = {}
        self.sig_p1s = {}
        self.sig_p2s = {}
        self.sig_names = {}
        self.sig_times = {} # 메모리 관리를 위해서 시간 정보를 저장함.
        self.plugins = plugins_path

        fl = glob.glob(plugins_path + os.sep + '*.s??')
        fl.sort()
        for name in fl:
            obj = p_md5_pattern_ext.search(name)
            if obj:
                idx = obj.groups()[0]
                sig_key = os.path.split(name)[1].lower().split('.')[0]
                sp = self.__load_sig(name)
                if sp is None:
                    continue

                if len(sp): # 만약 로딩된 악성코드 패턴이 1개 이상이라면?
                    if not (sig_key in self.sig_sizes):
                        self.sig_sizes[sig_key] = {}

                    for psize in list(sp):
                        if psize in self.sig_sizes[sig_key]:
                            self.sig_sizes[sig_key][psize].append(idx)
                        else:
                            self.sig_sizes[sig_key][psize] = [idx]




    # 지정한 악성코드 패턴에 해당 크기가 존재하는지 확인한다.
    
    # sig_key = 지정한 악성코드 패턴
    # sig_size = 크기
    # 악성코드 패턴 내부에 해당 크기가 존재하는지에 대한 여부 = 리턴값
    def match_size(self, sig_key, sig_size):
        sig_key = sig_key.lower()  # 대문자로 입력되어있을 가능성 때문에 모두 소문자로 변환시킨다.

        if sig_key in self.sig_sizes: # sig_key가 이미 로딩되어 있는지?
            if sig_size in self.sig_sizes[sig_key]:
                return True

        return False




    # 악성코드 패턴이 정상인지 검사한다.

    # sig_key = 지정한 악성코드 패턴
    # sig_size = 악성코드 패턴 크기
    # sig_md5 = 악성코드 MD5
    # 발견한 악성코드 이름 = 리턴값
    def scan(self, sig_key, sig_size, sig_md5):
        sig_key = sig_key.lower() # 대문자로 입력되어있을 가능성 때문에 모두 소문자로 변환시킴.

        if self.match_size(sig_key, sig_size): # 크기가 존재하는지?
            idxs = self.sig_sizes[sig_key][sig_size]  # 어떤 파일에 1차 악성코드 패턴이 존재하는지 확인함.

            fmd5 = sig_md5.decode('hex')
            sig_p1 = fmd5[:6] # 1차 악성코드 패턴
            sig_p2 = fmd5[6:] # 2차 악성코드 패턴

            for idx in idxs:
                # 1차 악성코드 패턴 비교를 진행한다.
                # 1 차 악성코드 패턴이 로딩되어 있지 않다면...
                if self.__load_sig_ex(self.sig_p1s, 'i', sig_key, idx) is False:
                    continue
                
                if sig_p1 in self.sig_p1s[sig_key][idx]:
                    p2_offs = self.sig_p1s[sig_key][idx][sig_p1]
                    
                    
                    # 2차 악성코드 패턴 비교를 진행함.
                    # 만약 2차 악성코드 패턴이 로딩되어 있지 않다면...
                    if self.__load_sig_ex(self.sig_p2s, 'c', sig_key, idx) is False:
                        continue


                    for off in p2_offs:
                        if self.sig_p2s[sig_key][idx][off] == sig_p2: # 2차 패턴 발견시!
                            if self.__load_sig_ex(self.sig_names, 'n', sig_key, idx) is False:
                                continue
                            return self.sig_names[sig_key][idx][off] # 악성코드 이름을 리턴함.

        self.__save_memory() # Anti-virus가 차지하는 메모리 용량을 낮추기 위해서 사용함.
        return None



    # 악성코드 패턴을 로딩한다.
    
    # fname = 악성코드 패턴 파일 이름, 악성코드 패턴 자료 구조 = 리턴값
    def __load_sig(self, fname):
        try:
            data = open(fname, 'rb').read()
            if data[0:4] == 'FVCM':
                sp = marshal.load(data[12:])
                return sp
        except IOError:
            return None




    # 악성코드 패턴을 로딩하는 모듈이다.
    
    # sig_dict = 악성코드 패턴이 로딩될 자료구조 
    # sig-prefix = 악성코드 패턴 이름중에 확장자 prefix가 저장되는 변수
    # sig_key = 악성코드 패턴 이름중에 파일이름이 저장되는 변수
    # idx = 악성코드 패턴 이름중에 파일 확장자 번호가 저장되는 변수
    # 리턴값 = 악성코드 패턴 로딩 성공 여부
    def __load_sig_ex(self, sig_dict, sig_prefix, sig_key, idx):
        if not (sig_key in sig_dict) or not (idx in sig_dict[sig_key]):
            try:
                name_fname = self.plugins + os.sep + '%s.%s%s' % (sig_key, sig_prefix, idx)
                sp = self.__load_sig(name_fname)
                if sp is None:
                    return False
            except IOError:
                return False

            sig_dict[sig_key] = {idx: sp}
        
        # 현재 시각을 sig_time에 기록하여 사용한다.    
        if not (sig_key in self.sig_times):
            self.sig_times[sig_key] = {}

        if not (sig_prefix in self.sig_times[sig_key]):
            self.sig_times[sig_key][sig_prefix] = {}

        self.sig_times[sig_key][sig_prefix][idx] = time.time()

        return True



    # 오랫동안 사용하지 않는 악성코드 패턴은 메모리에서 제거한다.
    def __save_memory(self):
        # 3분 기준으로 3분 이상 사용되지 않은 악성코드 패턴은 메모리에서 삭제함.
        n = time.time()
        for sig_key in self.sig_times.keys():
            for sig_prefix in self.sig_times[sig_key].keys():
                for idx in self.sig_times[sig_key][sig_prefix].keys():
                    if n - self.sig_times[sig_key][sig_prefix][idx] > 4:
                        if sig_prefix == 'i': # 1차 악성코드 패턴
                            self.sig_p1s[sig_key].pop(idx)
                        elif sig_prefix == 'c': # 2차 악성코드 패턴
                            self.sig_p2s[sig_key].pop(idx)
                        elif sig_prefix == 'n': # 악성코드 이름만을 정리한 패턴
                            self.sig_names[sig_key][sig_prefix].pop(idx)

                        self.sig_times[sig_key][sig_prefix].pop(idx)




    # 주어진 sig_key에 해당하는 악성코드 패턴의 누적된 수를 알려준다.
                    
    # sig_key = 악성코드 패턴 이름, 악성코드 패턴수 = 리턴값
    def get_sig_num(self, sig_key):
        sig_num = 0
        fl = glob.glob(self.plugins +os.sep + '%sn??' % sig_key)

        for fname in fl:
            try:
                buf = open(fname, 'rb').read(12)
                if buf[0:4] =='FVCM':
                    sig_num += get_uint32(buf, 4)
            except IOError:
                return None

        return sig_num




    # 주어진 sig_key에 해당되는 악성코드 패턴의 악성코드 이름을 알려준다.
    
    # sig_key = 악성코드 패턴 이름, 악성코드 이름 = 리턴값
    def get_sig_vlist(self, sig_key):
        sig_vname = []
        fl = glob.glob(self.plugins + os.sep + '%sn??' % sig_key)

        for fname in fl:
            try:
                sig_vname += self.__load_sig(fname)
            except IOError:
                return None

        return sig_vname





# 외부 라이브러리 소스코드 참고.
# https://gist.github.com/atdt/875e0dba6a15e3fa6018


FAIL = -1

class AhoCorasick:
    def __init__(self):
        self.transitions = {}
        self.outputs = {}
        self.fails = {}

    def make_tree(self, keywords):
        new_state = 0

        for keyword in keywords:
            state = 0

            for j, char in enumerate(keyword):
                res = self.transitions.get((state, char), FAIL)
                if res == FAIL:
                    break
                state = res

            for char in keyword[j:]:
                new_state += 1
                self.transitions[(state, char)] = new_state
                state = new_state

            self.outputs[state] = [keyword]

        queue = []

        for (from_state, char), to_state in self.transitions.items():
            if from_state == 0 and to_state != 0:
                queue.append(to_state)
                self.fails[to_state] = 0

        while queue:
            r = queue.pop(0)
            for (from_state, char), to_state in self.transitions.items():
                if from_state == r:
                    queue.append(to_state)
                    state = self.fails[from_state]

                    while True:
                        res = self.transitions.get((state, char), state and FAIL)
                        if res != FAIL:
                            break
                        state = self.fails[state]

                    failure = self.transitions.get((state, char), state and FAIL)
                    self.fails[to_state] = failure
                    self.outputs.setdefault(to_state, []).extend(
                        self.outputs.get(failure, []))


    def search(self, string):
        state = 0
        results = []
        for i, char in enumerate(string):
            while True:
                res = self.transitions.get((state, char), state and FAIL)
                if res != FAIL:
                    state = res
                    break
                state = self.fails[state]

            for match in self.outputs.get(state, ()):
                pos = i - len(match) + 1
                results.append((pos, match))

        return results



# 주어진 파일에서 지정된 영역에 대해 HexDump를 보여준다.

# fname = 파일명, start = 덤프할 영역의 시작 위치, size = 덤프할 크기, width = 한줄에 보여줄 문자의 개수
class HexDump:
    def File(self, fname, start, size=0x200, width=16):
        fp = open(fname, 'rb')
        fp.seek(start)
        row = start % width
        col = (start / width) * width
        r_size = 0
        line_start = row

        while True:
            if (r_size + (width - line_start) < size):
                r_char = (width - line_start)
                r_size += (width - line_start)
            else:
                r_char = size - r_size
                r_size = size

            line = fp.read(r_char)
            if len(line) == 0:
                break
            # 주소값 위치
            output = "%08X : " % col
            # Hex값 위치
            output += line_start * "   " \
                      + "".join("%02x " % ord(c) for c in line)

            output += line_start * " "
            output += "".join(['.', c][self.IsPrint(c)] for c in line)
            print output
            col += width
            line_start = 0
            if r_size == size:
                break
        fp.close()




    # 주어진 버퍼에 대해서 HexDump를 보여준다.
    
    # buf = 버퍼, start = 덤프할 영역의 시작 위치, size = 덤프할 크기, width = 한줄의 보여줄 문자의 갯수
    def Buffer(self, buf, start, size=0x200, width=16):
        # 주어진 크기보다 크면 버퍼가 작다면 인자값을 조정
        if len(buf) < size:
            size = len(buf)
        row = start % width  # 열
        col = (start / width)  # 행
        # [row ... width*col]
        # [width*col ... width * (col+1)]
        r_size = 0
        line_start = row + (col * width)
        # print hex(line_start), hex(width*(col+1))
        # print hex(row), hex(col)
        while True:
            line = buf[line_start:width * (col + 1)]

            if len(line) == 0:
                break
            if ((r_size + len(line)) < size):
                pass
            else:
                # print hex(line_start), hex(line_start + (size - r_size))
                line = line[0:(size - r_size)]
                r_size = size - len(line)
            # 주소 값
            output = "%08X : " % ((line_start / width) * width)
            # Hex 값
            output += row * "   " \
                      + "".join("%02x " % ord(c) for c in line)
            output += "  " \
                      + (width - (row + len(line))) * "   "
            # 문자 값
            output += row * " "
            output += "".join(['.', c][self.IsPrint(c)] for c in line)
            print output
            line_start = width * (col + 1)
            col += 1
            row = 0
            r_size += len(line)
            if r_size == size:
                break




    # 주어진 문자가 "출력 가능한 문자인지" 확인하는 함수.
    # 이 함수는 검사 대상 파일이 Text 파일인지 Binary 파일인지 확인하기 위함.
    
    # char = 문자 True = 출력 가능한 문자, False = 축력 불가능한 문자
    def IsPrint(self, char):
        c = ord(char)
        if c >= 0x20 and c < 0x80:
            return True
        else:
            return False



# HTML파일과 같은 텍스트로 차여있는 web server 구성 파일기반으로 제작된 
# 악성코드를 탐지하기 위헤서 먼저 파일의 내용을 꺼내어 텍스트 기반의 파일인지 확인함.
# 이 함수는 반드시 필요함.
# 악성코드 검사시, 검사대상 파일ㅣ WebShell이거나, 악성 페이지와 같은 경우에..

# 리턴값 = 텍스트 유무(True, False)
def is_textfile(buf):
    n_buf = len(buf)
    
    n_text = len(p_text.findall(buf))
    
    # 주어진 버퍼 내의서 해당 글자가 차지하는 비율이 80% 이상인지? 확인함.
    if n_text / float(n_buf) > 0.8:
        return True
    
    return False



# 버퍼에 의해 주어진 오프셋을 기준으로 uint16로 데이터를 읽어낸다.
# buf = 버퍼, off = 오프셋 uint16변환 값 = 리턴값
def get_uint16(buf, off):
    return struct.unpack('<H', buf[off:off+2])[0]

# 버퍼에 의해 주어진 오프셋을 기준으로 uint32로 데이터를 읽어낸다.
# buf = 버퍼, off = 오프셋 uint32변환 값 = 리턴값
def get_uint32(buf, off):
    return struct.unpack('<L', buf[off:off+4])[0]

# 버퍼에 의해 주어진 오프셋을 기준으로 uint64로 데이터를 읽어낸다.
# buf = 버퍼, off = 오프셋 uint64변환 값 = 리턴값
def get_uint64(buf, off):
    return struct.unpack('<Q', buf[off:off+8])[0]


# Feature 함수를 위한 로직 설계

class Feature:
    def __get_entropy(self, data):
        if not data:
            return 0
        
        entropy = 0
        for x in range(256):
            p_x = float(data.count(chr(x))) / len(data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
                
            return entropy
    
    def entropy(self, data):
        n_data = len(data)
        
        if n_data < 1024:
            data += '\x00' * (n_data % 256)
        else:
            data += '\x00' * (n_data % 256)
            
        mat_data = set()
        off = 0
        count = ((len(data) - 1024) / 256) + 1
        
        for i in range(count):
            t = data[off:off + 1024]
            n = int(self.__get_entropy(t) / 0.5)
            if n >= 16:
                n = 15
            for c in list(set(t)):
                mat_data.add(ord(c) / 2, n)
            off += 256
            
        m = [0] * 256
        for x, y in list(mat_data):
            seg, off = (x / 8), (x % 8)
            c |= (1 << off)
            m[(y * 16) + seg] = c
        
        ret = ''.join(map(chr, m))
        
        return ret
    
    def k_gram(selfself, data, k=2):
        charset = 'abcdefghijklmnopqrstuvwxyz0123456789()_-+=:,.'
        t_data = ''
        
        for c in data:
            if c in charset:
                t_data += c
    
        m = ['0'] * 2048
        for i in range(len(t_data) - 1):
            x, y = charset.index(t_data[i], charset.index(t_data[i + 1]))
            m[(y * 45) + x] = '1'
            
        m = ''.join(m)
        
        t_data = ''
        for i in range(2048 / 8):
            t_data += chr(int(m[i * 8:(i + 1) * 8], 2))
            
        return t_data
    
    
# FopxMain 클래스 선언

class FoxMain:
    def FreshPlugEnG(self, plugins_path, verbose=False):
        # 악성코드 패턴 초기화 요청
        global handle_pattern_md5
        handle_pattern_md5 = PatternMD5(plugins_path)
        
        return 0 # 악성코드 패턴 초기화 성공시에
    
    
    def DownPluginEnG(self): # 플러그인 엔진 종료
        return 0 # 플러그인 엔진 종료
    

    def GetInfoPlugEnG(self):
        info = dict()
        
        info['author'] = 'Nicht' # 플러그인 엔진 제작자
        info['version'] = '1.0' # 버전 명시
        info['title'] = 'Fox2Av Utility Library Module' # 엔진 설명
        info['fxm_name'] = 'FoxUtils' # 플러그인 엔진 파일 이름

        return info
