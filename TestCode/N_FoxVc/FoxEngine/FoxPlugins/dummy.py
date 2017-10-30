# _*_ coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com

import os, sys

class FoxMain():
    def FreshPlugEnG(self, plugin_path):
        self.Mal_Name = 'Dummy-Test-File (Not a Virus)'
        self.dummy_pattern = 'Dummy-Engine test-file'

        return 0

    def DownPlugEnG(self):
        del self.Mal_Name
        del self.dummy_pattern

        return 0

    def Scan(self, filehandle, filename):
        try:
            FilePattern = open(len(self.dummy_pattern))
            FilePattern.close()

            if buf == self.dummy_pattern:
                return True, self.Mal_name, 0
        except IOError:
            pass

        return False, '', -1

    def CureInfected(self, filename, Malware_ID):
        try:
            if Malware_ID == 0:
                os.remove(filename)
                return True
        except IOError:
            pass

        return False

    def VirusList(self):
        vlist = list()
        vlist.append(self.Mal_Name)

        return vlist

    def GetInfoPlugEnG(self):
        info = dict()

        info['author'] = 'Nicht; Lee Joon Sung'
        info['version'] = '1.0'
        info['title'] = 'Dummy Scan Engine'
        info['fxm_name'] = 'dummy'

        return info
