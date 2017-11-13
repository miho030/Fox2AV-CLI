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

class FileStruct:
    def __init__(self, filename=None, level=0):
        self.__fs = {}

        if filename:
            self.set_default(filename, level)

    def set_default(self, filename, level):
        import FoxKernel

        self.__fs['is_arc'] = False
        self.__fs['arc_engine_name'] = None
        self.__fs['arc_filename'] = ''
        self.__fs['filename_in_arc'] = ''
        self.__fs['real_filename'] = filename
        self.__fs['additional_filename'] = ''
        self.__fs['master_filename'] = filename
        self.__fs['is_modify'] = False
        self.__fs['can-arc'] = FoxKernel.MASTER_IGNORE
        self.__fs['level'] = level


    def is_archive(self):
        return self.__fs['is_arc']

    def get_archive_engine_name(self):
        return self.__fs['arc_engine_name']

    def get_filename_in_archive(self):
        return self.__fs['filename_in_arc']

    def -*- editing -*-