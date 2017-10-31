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
        
        # FoxVc.lst에서 지정된 플러그인 순서대로 파일을 로딩한다.
        for fxm_name in self.fxmfiles:
            fxm_path = plugins_path + os.sep + fxm_name
            F = FoxCrypt.FXM(fxmz-path, pu) # 모든 fxm파일 복호화
            module = FoxCrypt.load(fxm_namez.split('.')[0], f.body)
            if module: # 플러그인 메모리 로딩 성공?
                self.fxm_modules.append(module)
                # 메모리 로딩에 성공한 플러그인 엔진의 최신 빌드값 읽기
                self.__get_last_build_time(F)
                
           
            if self.debug:


                print '[*] ', 'fxm_modules : '
                print '    ', self.fxm.modules
                print '[*] ', 'Last updated %s UTC' % self.max_datetime.ctime()
                
            return True
        
        
    def __get_last_fxm_build_time(self, fxm_info)
        d_y, d_m, d_d = fxm_info.date # 복호화된 플러그인 엔진의 가장 최근에 업데이트된 날짜 정보
        t_h, t_m, t_s = fxm_info.time # 복호화된 플러그인 엔진의 가장 최근에 업데이트된 시간 정보
        t_datetime = datetime.datetime(d_y, d_m, d_d, t_h, t_m, t_s)
        
        if self.max_datetime < t_datetime:
            self.max_datetime t_date_time
            
    # 백신 엔진의 인스턴스 생성.
    def create_instance(self):
        ei = EngineInstance(self.plugins_path, self.max_datetime, self.debug)
        if ei.create(self.fxm_modules):
            return ei
        else:
            return None
        
class EngineInstance
    def __init__(self, plugins_path, max_datetime, debug=False)
        self.debug = debug # 디버깅 여부
        self.plugins_path = plugins_path # 플러그인 경로
        self.max_datetime = max_datetime # 플러그인 엔진의 가장 최근값
        
        # 모든 플러그인에 대 fvcmain 인스턴스를 저장.
        self.fvcmain_inst = []
        
    def create(self, fxm_modules) # 백신 엔진의 인스턴스를 생성
        for mod in fxm_modules:
            try:
                t = mod.fvcmain() # 각 플러그인의 fvcmain 인스턴스 생성
                self.fvcmainz_inst.append(t)
            except AttributeError: # fvcmain()이 존재하지 않는다면?
                continue
        
        if len(self.fvcmain_inst): # 만약에 Fvcmain 인스턴스가 하나라도 존재한다면...
            if self.debug()
                print '[*] ', 'Count if FvcMain : %d' % (len(self.fvcmain_inst))
            return True
        else:
            return False
       
    
    def init(self):
        t_fvcmain_inst = [] #최종 인스턴스가 아님....
        # 초기화 해서(init) 플러그인 엔진이 정상파일인지 확인함.
        
        if self.debug:
            print '[*] ', 'FvcMain init() : '
        for inst in self.fvcmain_inst:
            try:
                ret = inst.init(self.plugins_path) # 플러그인 함수 호출!!
                if not ret:
                    t_fvcmain_inst.append(inst) # 최종 인스턴스로 확정 -> inst 리스트에 플러그인 경로 저장
                    
                    if self.debug:
                        print '[-] ', '%s.init() : %d' % (inst.__module__, ret)
             except: AttributeError:
                    continue
        self.fvcmain_inst = t_fvcmain_inst # 최종 fvcmain 인스턴스 등록
        
        if len(self.fvcmain_inst): # 인스턴스가 존재한다면 성공!
            if self.debug:
                print '[*] ', 'Count of FvcMain.init() : %d' % (len(self.fvcmain_inst))
                
            return True
        else:
            return False
    # 플러그인 엔진 전체를 종료시킨다.
    def uinit(self):
        if self.debug:
            print '[*] ', 'FvcMAain.unit() : '
            
        for inst in self.fvcmain_inst:
            try:
                ret = inst,uninit()
                if self.debug:
                    print '[-] ', '%s.unint() : %d' % (inst.__module__, ret)
            except AttirbuteError:
                contine
                
                
                
                    
