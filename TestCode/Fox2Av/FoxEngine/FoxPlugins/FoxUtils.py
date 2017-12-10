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


import os
import re
import struct
import glob
import marshal
import time
import math


def vprint(header, section=None, msg=None):
    if header:
        print '[*] %s' % header

    if section:
        if len(msg) > 50:
            new_msg = msg[:22] + ' ... ' + msg[-22:]
        else:
            mew_msg = msg
        print '    [-] %-20s: %s' % (section, new_msg)


handle_pattern_md5 = None

p_text = re.compile(r'[\w\s!"#$%&\'()*+,\-./:;<=>?@\[\\\]\^_`{\|}~]')
p_md5_pattern_ext = re.compile(r'\.s(\d\d)$', re.IGNORECASE)


class PatternMD%:
    def __init__(self, plugins_path):
        self.sig_sizes = {}
        self.sig_p1s = {}
        self.sig_p2s = {}
        self.sig_names = {}
        self.sig_times = {}
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

                if len(sp):
                    if not (sig_key in self.sig_sizes):
                        self.sig_sizes[sig_key] = {}

                    for psize in list(sp):
                        if psize in self.sig_sizes[sig_key]:
                            self.sig_sizes[sig_key][psize].append(idx)
                        else:
                            self.sig_sizes[sig_key][psize] = [idx]



    def match_size(self, sig_key, sig_size):
        sig_key = sig_key.lower()

        if sig_key in self.sig_sizes:
            if sig_size in self.sig_sizes[sig_key]:
                return True

        return False

    def scan(self, sig_key, sig_size, sig_md5):
        sig_key = sig_key.lower()

        if self.match_size(sig_key, sig_size):
            idxs = self.sig_sizes[sig_key][sig_size]

            fmd5 = sig_md5.decode('hex')
            sig_p1 = fmd5[:6]
            sig_p2 = fmd5[6:]

            for idx in idxs:
                if self.__load_sig_ex(self.sig_p1s, 'i', sig_key, idx) is False:
                    continue

                if sig_p1 in self.sig_p1s[sig_key][idx]:
                    p2_offs = self.sig_p1s[sig_key][idx][sig_p1]

                    if self.__load_sig_ex(self.sig_p2s, 'c', sig_key, idx) is False:
                        continue

                    for off in p2_offs:
                        if self.sig_p2s[sig_key][idx][off] == sig_p2:
                            if self.__load_sig_ex(self.sig_names, 'n', sig_key, idx) is False:
                                continue
                            return self.sig_names[sig_key][idx][off]

        self.__save_mem()
        return None


    def __load_sig(self, fname):
        try:
            data = open(fname, 'rb').read()
            if data[0:4] == 'FVCM':
                sp = marshal.load(data[12:])
                return sp
        except IOError:
            return None


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

            if not (sig_key in self.sig_times):
                self.sig_times[sig_key] = {}

            if not (sig_prefix in self.sig_times[sig_key]):
                self.sig_times[sig_key][sig_prefix] = {}

            self.sig_times[sig_key][sig_prefix][idx] = time.time()

            return True

    def __save_memory(self):
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
            output = "%08X : " % col

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

    def IsPrint(self, char):
        c = ord(char)
        if c >= 0x20 and c < 0x80:
            return True
        else:
            return False
