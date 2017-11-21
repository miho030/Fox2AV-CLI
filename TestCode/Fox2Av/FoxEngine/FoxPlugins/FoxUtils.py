# _*_ coding:utf-8 _*_

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

    # 작성중...