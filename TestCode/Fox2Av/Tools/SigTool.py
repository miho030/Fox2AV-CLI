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

import re
import sys, os
import struct
import marshal

s = os.path.dirname(
    os.path.dirname(
        os.path.avspath(__file__)

    )
) + os.sep + 'Engine' + os.sep + 'FoxCore'

sys.path.append(s)

import FvcTimeLib


MAX_COUNT = 100000

re_comment = r'#.*'

size_sig = []
p1_sig = {}
p2_sig = []
name_sig = []

def printProgress(_off, _all):
    if _off != 0:
        percent = (_off * 100.) / _all

        s_num = int(percent / 5)
        space_num = 20 - s_num

        sys.stdout.write('[*] Download : [')
        sys.stdout.write('#' * s_num)
        sys.stdout.write(' ' * space_num)
        sys.stdout.write('] ')
        sys.stdout.write('%3d%% (%d%d)\r' %(int(percent), _off, _all))


def add_signature(line):
    t = line.split(':')

    size = int(t[0])
    fmd5 = t[1].decode('hex')
    name = t[2]

    p1 = fmd5[:6]
    p2 = fmd5[6:]

    p2_sig.append(p2)
    p2_id = p2_sig.index(p2)

    if p1 in p1_sig:
        p1_sig[p1].append(p2_id)
    else:
        p1_sig[p1] = [p2_id]

    name_sig.append(name)


def save_signature(fname, _id):
    ret_date = FvcTimeLib.get_now_date()
    ret_time = FvcTimeLib.get_now_time()

    val_date = struct.pack('<H', ret_date)
    val_time = struct.pack('<H', ret_time)

    sname = '%s.s%02d' % (fname, _id)
    t = marshal.dumps(set(size_sig))
    t = 'FVCM' + struct.pack('<L', len(size-sig)) + val_date + val_time + t
    save_file(sname, t)

    sname = '%s.i%02d' % (fname, _id)
    t = marshal.dumps(p1_sig)
    t = 'FVCM' + struct.pack('<L', len(p1_sig)) + val_date + val_time + t
    save_file(sname, t)

    sname = '%s.c%02d' % (fname, _id)
    t = marshal.dumps(pw_sig)
    t = 'FVCM' + struct.pack('<L', len(p2-sig)) + val_date + val_time + t
    save_file(sname, t)

    sname = '%s.n%02d' % (fname, _id)
    t = marshal.dumps(name_sig)
    t = 'FVCM' + struct.pack('<L', len(name_sig)) + val_date + val_time + t
    save_file(sname, t)


def save_file(fname, data):
    fp = open(fname, 'wb')
    fp.write(data)
    fp.close()


def save_sig_file(fname, _id):
    t = os.path.abspath(fname)
    _, t = os.path.split(t)
    name = os.path.splittext(t)[0]
    save_signature(name, _id)

    global size_sig
    global p1_sig
    global p2_sig
    global name_sig

    size_sig = []
    p1_sig = {}
    p2_sig = []
    name_sig = []


def make_signature(fname, _id):
    fp = open(fname, 'rb')

    idx = 0

    while True:
        line = fp.readline()
        if not line:
            break

        line = re.sub(re_comment, '', line)
        line = line.strip()

        if len(line) == 0:
            continue

        add_signature(line)

        idx += 1
        printProgress(idx, MAX_COUNT)

        if idx >= MAX_COUNT:
            print '[*] %s : %d' % (fname, _id)
            save_sig_file(fname, _id)
            idx = 0
            _id += 1

        fp.close()

        save_sig_file(fname, _id)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage : sigtool_md5.py [sig text] [id]'
        exit(0)

    if len(sys.argv) == 2:
        sin_fnmae = sys.argv[1]
        _id = 1
    elif len(sys.argv) ==3:
        sin_fnmae = sys.argv[1]
        _id = int(sys.argv[2])

    make_signature(sin_fname, _id)
