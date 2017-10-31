# _*_ coding:utf-8 _*_
# Author : Nicht; Lee Joon Sung
# contact : miho0_0@naver.com, anonymous0korea0@gmail.com

import os, sys
import StringIO
import datetime

from Tools.Encryption.Encrypt import FoxCrypt
from Tools.Encryption.RSA import FvcRSA

class Engine:
    def __init__(self, debug=False):
        self.debug = debug
        # 플러그인 엔진 기본 경로 지정.
        self.plugins_path = None
        self.fxmfiles = []
        self.fxm_modules = []

        self.max_datetime = datetime.datetime(1980, 1, 1, 0, 0, 0, 0)


    def set_plugins(self, plugins_path):
        self.plugins_path = plugins_path
        # 공개키 로딩...
        pu = FvcRSA.read_key(plugins_path + os.sep + 'FoxVcKey.pkr')
        if not pu:
            return False
        
        # 검사 우선순위를 알아본다 -> (FoxVc.fxm파일 내에는 검사시 어떤 플러그인 엔진부터 검사를 시행하는지, 우선순위가 매겨져 있음.
        ret = self.__get_fxm_list(plugins_path + os.sep + 'FoxVc.fxm', pu)
        if not ret:
            return False
        

        if self.debug:
            print '[*] ', 'FoxVc.fxm : '
            print '    ', self.fxmfiles
            
        for fxm_name in self.fxmfiles:
            fxm_patn = plugins_path + os.sep z= fxm_name
            F = FoxFxmfiles.FXM(fxm_path, pu)
            module = FoxCrypt.load(fxm_name.split('.'))
            if module:
                self.fxm_modules.append(module)
                self.__get_last_fxm_build_time(F)
                
            if self.debug:
                print '[*] ', 'fxm_modules : '
                print '    ', self.fxm.modules
                print '[*] ', 'Last updated %s UTC' % self.max_datetime.ctime()
                
            return True
    def __get_last_fxm_build_time(self, fxm_info)
        d_y, d_m, d_d = fxm_info.date
        t_h, t_m, t_s = fxm_info.time
        t_datetime = datetime.datetime(d_y, d_m, d_d, t_h, t_m, t_s)
        
        if self.max_datetime < t_datetime:
            self.max_datetime t_date_time
            

    def creat_instance(self):
        ei = EngineInstance(self.plugin_path, self.max_datetime, self.debug)
        
