# _*_ coding:utf-8 _*_
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

class Fox_File_Structure:
    def __init__(self, filename=None, level=0):
        self.__fs = {}

        if filename:
            self.set_default(filename, level)

    def Fox_set_default(self, filename, level):
        import FoxKernel

        self.__fs['is_arc'] = False
        self.__fs['arc_engine_name'] = None
        self.__fs['arc_filename'] = ''
        self.__fs['filename_in_arc'] = ''
        self.__fs['real_filename'] = filename
        self.__fs['additional_filename'] = ''
        self.__fs['master_filename'] = filename
        self.__fs['is_modify'] = False
        self.__fs['can_arc'] = FoxKernel.MASTER_IGNORE
        self.__fs['level'] = level


    # 파일에 대해서 압축 가능한지 압축 여부를 질의한다.
    def is_Fox_can_archive(self):
        return self.__fs['is_arc']


    # 실제 압축 해제가 가능한 엔진을 확인한다.
    def is_any_Fox_get_archive_engine_name(self):
        return self.__fs['arc_engine_name']


    # 실제 압축 파일명을 확인한다.
    def is_Fox_get_archive_filename(self):
        return self.__fs['filename_in_arc']


    # 압축파일 대상의 파일명을 확인한다.
    def is_Fox_get_filename_in_archive(self):
        return self.__fs['filename_in_arc']


    # 실제 작업 대상 파일의 이름을 확인한다.
    def is_Fox_get_filename(self, fname):
        return self.__fs['real_filename']


    def Foxes_are_setting_filename(self, fname):
        self.__fs['real_filename'] = fname


    # 압축파일의 최상위 파일명을 확인한다.
    def is_Fox_get_master_filename(self):
        return self.__fs['master_filename']


    # 압축파일 내부를 표현하기 위해서 실제 파일이름을 확인한다.
    def is_Fox_get_additional_filename(self):
        return self.__fs['additional_filename']


    # 압축 파일 내부의 표현을 위한 실제 파일이름들을 세팅한다.,
    def Foxes_are_setting_additional_filename(self, filename):
        self.__fs['additional_filename'] = filename


    # 악성코드 치료로 인해 파일이 수정된 경우에 대비하기 위해, 파일수정여부를 확인한다.
    def is_Fox_modify(self):
        return self.__fs['is_modify']


    # 악성코드 치료로 파일의 수정여부를 저장함.
    def Foxes_are_setting_modify(self, modify):
        self.__fs['is_modify'] = modify


    # 악성코드 치료 후에 파일을 재압축 할 수 있는지에 대한 여부를 확인한다.
    def Fox_get_can_archive(self):
        return self.__fs['can_arc']


    # 악성코드 치료 후에 파일을 재압축 할 수 있는지에 대한 설정을 한다.
    def Foxes_are_setting_archive(self, mode):
        self.__fs['can_arc'] = mode


    # 검사 대상 압축파일의 깊이를 알아낸다.
    def is_Foxes_are_getting_level(self):
        return self.__fs['level']


    # 검사 대상 압축파일의 깊이를 설정한다.
    def Foxes_are_setting_level(self, level):
        self.__fs['level'] = level



#=======================================================================================================#
    # 주어진 정보를 이용하여 파일 정보를 저장한다!

    # 주요 변수들...
    """
    engine_ID = 압축 해제 가능한 엔진의 ID값
    Rname = 검사 대상이 되는 압축파일
    Fname = 압축해제 대상 파일
    Dname = 압축 파일의 내부를 표현하기 위한 파일 이름(임의)
    Mname = 마스터 파일(최상위 파일의 이름임.)
    modify = 악성코드 치료로 인해 파일이 수정되었는지..?
    can_arc = 악성코드 치료 후, 폴더와 파일들을 원래의 모습으로 되돌리기 위해, 재압축이 가능한지? 
    level = 압축 깊이
    
    """
# =======================================================================================================#
    def Foxes_are_setting_archive_imao(self, engine_ID, Rname, Fname, Dname, Mname, modify, can_arc, level):
        # 검사 대상 파일이, 압축되어 있는지?
        self.__fs['ia_arc'] = True
        # 압축되어 있다면 압축을 해제할 수 있는 플러그인 엔진이 존재하는지?
        self.__fs['arc_engine_name'] = engine_ID
        # 실제 압축파일(검사 대상 파일)
        self.__fs['arc_filename'] = Rname
        # 압축해제 대상 파일
        self.__fs['filename_in_arc'] = Fname
        # 검사 대상파일
        self.__fs['real_filename'] = ''
        #압축 파일의 내부를 표현하기 위한 임시 파일명..
        self.__fs['additional_filename'] = Dname
        # 마스터파일(최상위 파일의 이름)
        self.__fs['master_filename'] = Mname
        #악성코드 치료로 인해 파일이 수정되었는지?
        self.__fs['is_modify'] = modify
        # 재압축 가능한지?
        self.__fs['can_arc'] = can_arc
        # 재압축 깊이?
        self.__fs['level'] = level
