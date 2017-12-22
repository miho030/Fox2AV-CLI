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




    # 압툭을 하였으면 재압축을 해야지!
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
