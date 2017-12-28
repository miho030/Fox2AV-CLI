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

"""
편의상 주석문 미작성함.
향후 여유가 생기면 주석문 작성 예정임.

"""

import re
import os
import hashlib

import FoxUtils
from FoxEngine.FoxCore import FoxKernel

class FoxMain:
    # 플러그인 엔진을 모두 초기화 시킨다. verbose값 -> 디버깅 여부
    def FreshPlugEnG(self, plugins_path, vervose=False):
        # 파일 내부에 파일 데이터가 <script, <iframe으로 시작하는지 확인하는 정규 표현식
        self.p_script_head = re.compile(r'\s*<\s*(script|iframe)', re.IGNORECASE)

        # script/iframe 정보가  html파일 내부에 존재하는지 확인하는 정규 표현식이다.
        s = r'<\s*(script|ifrmae).*?>([\d\D]*?)<\s*/(script|ifrmae)\s*>'
        self.p_script_in_html = re.compile(s, re.IGNORECASE)

        # 주석문 및 공백 제거를 위한 정규표현힉임.
        self.p_http = re.compile(r'https?://')
        self.p_script_cmt1 = re.compile()
        self.p_script_cmt2 = re.compile(r'/\*.*?\*/', re.DOTALL)
        self.p_script_cmt3 = re.compile(r'(#|\bREM\b).*', re.IGNORECASE)
        self.p_space = re.compile(r'\s')

        return 0

    # 플러그인 엔진을 종료시킨다.
    # 리턴값 0일 시에 성공임.
    def DownPlugEnG(self): #플러그인 엔진 종료
        return 0 # 플러그인 엔진 종료 성공


    def GetInforPlugEnG(self):
        info = dict()

        info['author'] = 'Nicht' # 제작자
        info['version'] = '1.0' # 엔진 버전
        info['title'] = 'Script Engine' # 엔진 설명
        info['fxm_name'] = 'script' # 엔진 파일 이름
        info['sig_num'] = FoxUtils.handle_pattern_md5.get_sig_num('script') # 진단 가능한 악성코드 수, 종류


    # 진단,치료 가능한 악성코드의 리스트를 알려준다.
    # 리턴값은 당연히 악성코드 리스트!
    def listvirus(self): # 진단 가능한 악성코드 리스트
        vlist = FoxUtils.handle_pattern_md5.get_sig_vlist('script')
        vlist.sort()
        return vlist


    # 파일 포맷을 분석하는 함수
    # 입력값 ...:
    #           filehandle = 파일 핸들
    #           filename = 파일 이름
    #           filename_ex = 압축 파일 내부 파일 이름
    #
    #리턴값 ...:
    #           파일 포맷 분석 정보 or None
    # 파일 포맷 분석 함수 ~
    def format(self, filehandle, filename, filename_ex):
        fileformat = {}

        mm = filehandle

        buf = mm[:4096]
        if FoxUtils.is_textfile(buf): # 스크립트 파일이 아닌 Text파일인지 FoxUtils모듈에게 질의함.
            obj = self.p_script_head.match(buf)
            if obj:
                # 내부 스크립트가 존재하는지 질의하는 함수 구현...
                obj_script = self.p_script_in_html.search(mm[:])

                if obj_script:
                    buf_strip = obj_script.groups()[1].strip()
                    n_buf_stript = len(buf_strip)
                    fileformat['size'] = n_buf_stript

                    # 엥 스크립트가 존재하잖아?! -> if n_buf_stript로 긔긔
                    if n_buf_stript: # 내부 스크립트 확인할 때...
                        # 내부 스크립트...
                        if obj_script.groups()[0].lower() == 'script':
                            ret = {'ff_script': fileformat}
                        else:
                            ret = {'ff_ifrmae': fileformat}
                        # 외부 스크립트...
                    else:
                        # 외부 스크립트도 확인한다.
                        if obj_script.groups()[0].lower() == 'script':
                            ret = {'ff_script_external': fileformat}
                        else:
                            ret = {'ff_ifrmae_external': fileformat}
                # 만약 내부 스크립트를 발견하지 못했다면.. 외부 스크립트 일 가능성이 크다.
                else:
                    fileformat['size'] = 0 # 외부 스크립트로 처리.

                    if obj.groups().lower().find('script') != -1:
                        ret = {'ff_script_external': fileformat}
                    else:
                        ret = {'ff_ifrmae_external': fileformat}

                return ret

        return None



    # 압축파일 내부의 파일 목록을 얻는다.
    # 여기서는 스크립트 내부의 데이터를 내부 파일 목록으로 지정하여 사용.
    # 기존에 만들어놨던 압축파일 악성코드 검사/피료 모듈을 그대로 적용하여 사용하였음.
    # 기존의 모듈들은...
    #       파일 = script
    #       압축 파일 내부 파일 목록 = script, iframe등 스크립트 파일임을 파악할 수 있는 문자열의 존대여부와 개수
    #
    #
    # 리턴값은 당연히...![압축엔진 ID, 압축된 파일 이름]
    def arclist(self, filename, fileformat):
        file_scan_list = [] # 검사 대상의 모든 정보를 저장한다.

        # 미리 분석된 파일 포맷 중에 ff_script 포맷이 있는지 질의!
        if 'ff_script' in fileformat:
            # TODO : VBSScript에 대한 처리도 필요하다!!
            file_scan_list.append(['arc_script', 'JavaScript'])
        elif 'ff_ifrmae' in fileformat:
            file_scan_list.append(['arc_ifrmae', 'IFrame'])

        return file_scan_list



    # 압축 모듈의 명령을 따라서 파일의 압축을 해제한다.
    # 여기서는 압축이 아니라 파일 내부의 데이터인 html코드를 추출하도록한다..
    #
    # 리턴값은 당연히...![압축 해제된 파일(스크립트)의 내용 Or None]
    def unarc(self, arc_engine_id, arc_name, fname_in_arc):
        if arc_engine_id == 'arc_script' or arc_engine_id == 'arc_ifrmae':
            buf = ''

            try:
                with open(arc_name, 'rb') as fp:
                    buf = fp.read()
            except IOError:
                return None

            obj = self.p_script_in_html.search(buf)
            if obj:
                data = obj.groups()[1]
                return data

        return None


    # 입측파일 핸들을 종료한다.
    # 말 그대로임. ㅇㅇ
    def arcclose(self):
        pass




    # 압축을 하였으면 재압축을 해야지!
    # 기존 압축파일 악성코드 진단/치료 모듈의 형식상 그대로 구현하기로했다.
    #
    # 리턴값은 당연히...![암축 성공 여부!]
    def mkarc(self, arc_engine_id, arc_name, file_infos):
        if arc_engine_id == 'arc_script' or arc_engine_id == 'arc_ifrmae':
            #기존 파일에서 각 스크립트들의 위치 정보를 알아내어야 한다.!!!
            all_script_info = []
            buf = ''

            try:
                with open(arc_name, 'rb') as fp:
                    buf = fp.read()
            except IOError:
                return False

            obj = self.p_script_in_html.search(buf)

            if obj:
                t = obj.group()
                pos = obj.span()

                all_script_info.append(['script', pos, t])

                org_buf = buf

                # 처음 부터 순차적으로 파일 내용을 교체하여 저장한다.
                for idx, file_info in enumerate(file_infos):
                    rname = file_info.get_filename()
                    try:
                        if os.path.exists(rname): # 치료된 파일이 존재하는지?
                            with open(rname, 'rb') as fp:
                                buf = fp.read()

                                if len(all_script_info[idx][2]) < len(buf):
                                    return False

                                buf += ' ' * (len(all_script_info[idx][2]) - len(buf))
                                all_script_info[idx][2] = buf
                        else:
                            buf = ' ' * len(all_script_info[idx][2])
                            all_script_info[idx][2] = buf
                    except IOError:
                        pass


                # 모든 데이터를 합쳐서 원본 파일로 복구하기.
                fp = open(arc_name, 'wb')
                start_pos = 0
                for script_info in all_script_info:
                    pos = script_info[1]
                    buf = org_buf[start_pos:pos[0]]
                    fp.write(buf)
                    fp.write(script_info[2])
                    start_pos = pos[1]
                else:
                    fp.write(org_buf[start_pos:])

                fp.close()
                return True

        return False


    # 악성코드를 검사하는 모듈. 스크립트 내부의 악성코드가 존재하는지 확인함.
    # filehandle = 파일 핸들, filename = 파일 이름, fileforamt = 파일 포맷, filename_ex = 파일 이름(압축 내부 데이터)
    # 리턴값 = [악성코드 발견 여부, 악성코드 이름, 악성코드 ID]
    def scan(self, filehandle, filename, fileformat, filename_ex): # 악성코드 검사 시작
        try:
            mm = filehandle

            if not ('ff_html' in fileformat or
                    'ff_script' in fileformat or
                    'ff_ifrmae' in fileformat or
                    'ff_script_external' in fileformat or
                    'ff_ifrma_externel' in fileformat):

                raise ValueError # 해당 포맷이 포함되어 있을 때만 script 엔진 검사 실행.

            if FoxUtils.is_textfile(mm[:4096]):
                buf = mm[:]

                buf = self.p_http.sub('', buf) # http:// 제거하기.
                buf = self.p_script_cmt1.sub('', buf) # 스크립트 파일 내분의 모든 주석문 제거

                # 두 주석문이 보일 때만 제거 작업 실행 -> 처리 속도를 빠르게 하기위해서..
                pos2 = -1
                pos1 = buf.find('/*')
                if pos1 != -1:
                    pos2 = buf.rfind('/*')

                if 0 <= pos1 < pos2:
                    buf = self.p_script_cmt2.sub('', buf) # 주석문 제거 실시

                buf = self.p_script_cmt3.sub('', buf)
                buf = self.p_space.sub('', buf)
                buf = buf.lower() # 영어 소문자로 통일시키기

                size = len(buf)
                # script 패턴에서 지정된 해당 크기가 존재하는지
                if FoxUtils.handle_pattern_md5.match_size('script', size):
                    fmd5 = hashlib.md5(buf).hexdigest() # Md5 해시 구하기 -> 한줄로
                    # .. 스크립트 패턴에서 MD5해시 검사 실시.
                    vname = FoxUtils.handle_pattern_md5.scan('script', size, fmd5)
                    if vname:
                        return True, vname, 0, FoxKernel.INFECTED
        except IOError:
            pass
        except ValueError:
            pass

        return False, '', -1, FoxKernel.NOT_FOUND


    def CureInfected(self, filename, malware_ID): # 악성코드 치료..
        try:
            # 악성코드 진단 결과에서 받은 malware_ID 값이 0인가?
            if malware_ID == 0:
                os.remove(filename) #악성코드 삭제 시도
                return True # 악성코드 치료 완료시 리턴함.
        except IOError:
            pass

        return False # 악성코드 치료 실패..
