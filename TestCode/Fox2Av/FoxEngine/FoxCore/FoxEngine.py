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

import StringIO
import datetime
import glob
import imp
import os
import re
import struct
import tempfile
import types
import FoxConst
import FvcFile
import FvcTimeLib

from FoxEngine.FoxCore.FoxEncryption.FoxCryptionTools import FvcCrypto
from FoxEngine.FoxCore.FoxEncryption.FoxRSA import FvcRSA


# Definite Engine Error Mes.
class EngineKnownError(Exception):
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return repr(self.value)


# definite Engine Class
class Engine:
    def __FreshPlugEnG__(self, verbose=False): # 플러그인 엔진 초기화 => 플러그인 엔진의 무결성, 위/변조 방지 위한 검사.
        self.verbose = verbose # 디버깅 여부 확인

        self.plugins_path = None # 플러그인 경로 설정
        self.fxmFiles = []
        self.fxm_modules = []

        # 플러그인의 가장 최근의 시간 값을 저장.
        # 초기값은 1980-01-01이다.
        self.max_datetime = datetime.datetime(1980, 1, 1, 0, 0, 0, 0)

        # 백신이 구동되면서 만든 임시 파일을들 모두 제거한다.
        self.__remove_Fvc_Temfile()




    # 임시 파일 제거를 위한 함수...
    def __remove_Fvc_TempFile(self):
        tpath = tempfile.gettempdir()
        fI = glob.glob(tpath + os.sep + 'ftmp*') # ftmp라는 확장자를 지정.
        for name in fI: # FI(ftmp확장자를 보유한 파일)이 존재하는지 확인..
            if os.path.isfile(name): # 만약 파일이 발견 된다면?
                try:
                    os.remove(name) # 응 삭제~
                except IOError:
                    pass
                except WindowsError:
                    pass




    # 지정된 경로(plugins_path)내에서 플러그인 엔진을 로딩하기 위한 기초 설정을 마무리한다.
    def set_plugins(self, plugins_path):
        # 플러그인 경로 지정.
        self.plugins_path = plugins_path

        # 플러그인 엔진 로딩 시에 어떤 엔진을 먼저 로딩할지 우선 순위을 조사한다.
        # 이는 악성코드 진단/치료시에 빠른 대처를 위함.
        if FoxConst.FVCDEBUG:
            pu = None
            ret = self.__get_fxm_list(plugins_path  + os.sep + 'FoxVcList.lst', pu)
        else:
            # FvcRSA,FvcCrypt.에서 생성한 rsa 공개키와 개인키 중,
            # 공개키(FoxVcKey.pkr)을 백신 커널에 로딩한다.
            pu = FvcRSA.read_key(plugins_path + os.sep + 'FoxVcKey.pkr')
            if not pu:
                return False

            ret = self.__get_fxm_list(plugins_path + os.sep + 'FoxVcList.fxm', pu)

        if not ret: # 만약 암호화된 FoxVcList.fxm 파일이 없다면...
            return False

        if self.verbose:
            print '[*] FoxVcList.%s : ' % ('lst' if FoxConst.FVCDEBUG else 'fxm')
            print '   ', self.fxmFiles

        # FoxVc.lst에 존재하는 데이터를 기반으로 FXM파일을 로딩한다.
        for fxm_name in self.fxmFiles:
            fxm_path = plugins_path + os.sep + fxm_name
            try:
                name = fxm_name.split('.')[0]
                if FoxConst.FVCDEBUG:
                    f = None
                    module = imp.load_source(name, fxm_path.rsplit('.')[0] + '.py')
                    try:
                        os.remove(fxm_path.rsplit('.')[0] + '.pyc')
                    except WindowsError:
                        pass
                else:
                    f = FvcCrypto.KMD(fxm_path, pu) # 모든 fxm파일을 복호화함 -> 암호화된 플러그인 엔진들을 모두 복호화시킴.
                    data = f.body
                    module = FvcCrypto.load(name, data)

                if module: # 플러그인들을 메모리에 로딩 성공했을 시에..
                    self.fxm_modules.append(module)
                    # 메모리 로딩에 성공한 fxm파일에서 플러그인엔진의 가장 최근 시간 값 읽기
                    # 이 날짜는 최신 업데이트 날짜가 된다.
                    self.__get_last_fxm_build_time(f)
            except IOError:
                pass
            except FvcCrypto.FXMFormatError:
                pass


        # 악성코드 패턴에서 최신 시간값을 구한다.
        f1 = glob.glob(plugins_path + os.sep + '*.n??')
        for fname in f1:
            try:
                buf = open(fname, 'rb').read(12)
                if buf[0:4] == 'FVCM':
                    sdate = FvcTimeLib.convert_date(struct.unpack('<H', buf[8:10])[0])
                    stime = FvcTimeLib.convert_time(struct.unpack('<H', buf[10:12])[0])
                
                    t_datetime = datetime.datetime(sdate[0], sdate[1], sdate[2], stime[0])
                
                    if self.max_datetime < t_datetime:
                        self.max_datetime = t_datetime
            except IOError:
                pass
                 
        if self.verbose:
            print '[*] fxm_modules :'
            print '   ', self.fxm_modules
            print '[*] Last updated %sUTC' % self.max_datetime.ctime()
            
        return True




    # 백신 엔진의 인스턴스를 생성한다.
    def create_instance(self):
        ei = EngineInstance(self.plugins_path, self.max_datetime, self.verbose)
        if ei.create(self.fxm_modules):
            return ei
        else:
            return None




    # 복호화된 플러그인 엔진의 시간 값중 가장 최근 시간값을 보관한다.
    # 이는 플러그인 엔진의 Lasteset-version-date 로 인식.
    def __get_last_fxm_build_time(self, fxm_info):
        if FoxConst.FVCDEBUG:
            t_datetime = datetime.datetime.utcnow()
        else:
            d_y, d_m, d_d = fxm_info.date
            t_h, t_m, t_s = fxm_info.time
                
            t_datetime = datetime.datetime(d_y, d_m, d_d, t_h, t_m, t_s)
            
        if self.max_datetime < t_datetime:
            self.max_datetime = t_datetime



    def __get_fxm_list(self, Fox2AV_fxm_file, pu):
        fxmfiles = [] # 우선순위 목록
    
        if FoxConst.FVCDEBUG: # 디버깅 상태에선 복호화 없이 파일을 읽어온다!
            lst_data = open(Fox2AV_fxm_file, 'rb').read()
        else:
            f = FvcCrypto.FXM(Fox2AV_fxm_file, pu) # FoxVc.fxm 파일을 복호화 시킨다.
            lst_data = f.body
            
        # FoxVc.fxm 파일이 제대로 인식이되어 읽혔는가?
        if lst_data:
            msg = StringIO.StringIO(lst_data)
            

            while True:
                # 버퍼 한줄을 읽어 엔터키(\n)제거
                line = msg.readline().strip()

                # 잃혀진 내용이 존재하지 않으면 Halt.
                if not line:
                    break
                elif line.find('.fxm') != -1: # 만약 fxm 확장자를 가진 파일이 존재한다면...
                    fxmfiles.append(line) # fxm 우선 순위 목록에 추가함 -> lst 갱신 귀찮앙...
                else: # fxm을 가진 확장자가 아닐시에..
                    continue

        # 우선순위 목록이 하나라도 존재한다면 앙 성공띠
        if len(fxmfiles):
            self.fxmfiles = fxmfiles
            return True
        else: # 우선 순위 목록에 아무것도 없으면 앙 실패띠..
            return False




class EngineInstance:
    def __init__(self, plugins_path, max_datetime, verbose=False):
        self.verbose = verbose # 디버깅 여부
        
        self.plugins_path = plugins_path # 플러그인 경로를 저장함.
        self.max_datetime = max_datetime # 플러그인 엔진의 가장 최신 시간/날짜 값
        
        self.options = {} # 옵션..
        self.set_options() # 기본 옵션을 설정하기 위한 변수
        
        self.FoxMain_inst = [] # 모든 플러그인 엔진의 FoxMain 인스턴스..
        self.update_info = [] # 압축 파일 최종 치료를 위한 업데이트 갱신 데이터가 담긴 리스트.

        self.result = {} # 결과 값.
        self.identified_virus = set() # 특정한 악성코드 갯수를 구할 때 사용.
        self.set_result() # 악성코드 검사 결과를 reset한다.
    
        self.disinfect_callback_fn = None # malware CureInfect Callback Function.
        self.update_callback_fn = None # Malware arc CureInfect Callback Function.
        self.quarantine_callback_fn = None # Malware  격리 콜백 함수
    
        self.disable_path = re.compile(r'/<\w+>')



    # 백신 엔진 인스턴스 생성
    def create(self, fxm_modules):
        for mod in fxm_modules:
            try:
                t = mod.FoxMain() # 각 플러그인 엔진내에 FoxMain 인스턴스 생성
                self.FoxMain_inst.append(t)
            except AttributeError: # FoxMain 클래스가 존재하지 않음을 알림.
                continue

        if len(self.FoxMain_inst): # FoxMain 인스턴스가 하나라도 존재하면   앙 성공띠
            if self.verbose:
                print '[*] Count of FoxMain : %d' % (len(self.FoxMain_inst))
            return True
        else:
            return False


    # init 명령어를 사용하여 각 플러그인 엔진들이 정상적으로 초기화를 실행하는지 확인
    # 만약 실패시, 최종 플러그인 인스턴스 리스트에서 삭제 --> cuz 향후 어떤 함수의 실행도 무의미해지기 때문이다.
    def FreshPlugEnG(self):
        #init 명령어를 사용하여 실행 후 정상이라고 판단된 플러그인만 최종 등록하여 인스턴스를 생성.
        t_FoxMain_inst = [] # 최종 플러그인 인스턴스 리스트

        if self.verbose: # 디버깅 여부                           앙 여우띠!
            print '[*] FoxMain.FreshPlugEnG :'
        
        for inst in self.FoxMain_inst:
            try:
                # 플러그인 엔진의 init 함수 호출
                ret = inst.FreshPlugEnG(self.plugins_path, self.options['opt_veerbose'])
                if not ret:
                    t_FoxMain_inst.append(inst)

                    if self.verbose:
                        print '.   [-] %s.FreshPlugEnG() : %d' % (inst.__module__, ret)
            except AttributeError:
                continue

        self.FoxMain_inst = t_FoxMain_inst # 정상이라고 판단된 플러그인을 최종 인스턴스에 등록..
    
        if len(self.FoxMain_inst):
            if self.verbose:
                print '[*] Count of FoxMain.FreshPlugEnG() :%d' % (len(self.FoxMain_inst))
            return True
        else:
            return False



    # 플러그인 엔진 Halt.
    def DownPlugEnG(self):
        if self.verbose: # 디버깅 여부      앙 여우띠!!!!!
            print '[*] FoxMain.DownPlugEnG() : '
        
        for inst in self.FoxMain_inst:
            try:
                ret = inst.DownPlugEnG()
                if self.verbose:
                    print '    [-] %s.DownPlugEnG() : %d' % (inst.__module__, ret)
            except AttributeError:
                continue


    # 플러그인 엔진의 정보를 얻어온다.
    def GetInfoPlugEnG(self):
        ginfo = [] # 플러그인 엔진의 정보를 담는 리스트.

        if self.verbose: # 디버깅 여부                        앙 여우띠!!
            print '[*] FoxMain.GetInfoPlugEnG() :'
        
        for inst in self.FoxMain_isnt:
            try:
                ret = inst.GetInfoPlugEnG()
                ginfo.append(ret)

                if self.verbose:
                    print '    [-] %s.GeInfoPlugEnG() :' % inst.__module__
                for key in ret.keys():
                    print '         - %-10s : %s' % (key, ret[key])
            except AttributeError:
                continue

        return ginfo




    # 각 플러그인 엔진이 진단 할 수 있는 악성코드 목록을 얻어온다.
    # 이는 소비자가 각 플러그인엔진이 얼마나, 어떤, 악성코드를 진단하고 치료할 수 있는지 파악하는데 도움이됨.
    def VirusList(self, *callback):
        vlist = [] # 진단/치료 가능한 악성코드 목록 리스트.
    
        argc = len(callback) # 가변인자 확인
        
        if argc == 0: # 인자가 존재하지 않는다면...?
            cb_fn = None
        elif argc == 1: # Callback 함수가 존재하는지...?
            cb_fn = callback[0]
        else: # 인자가 너무 많으면 에러로 표기.
            return []

        if self.verbose: # 디버깅 여부                                                  앙 여우띠
            print '[*] FoxMain.VirusList() :'

        for inst in self.FoxMain_inst:
            try:
                ret = inst.VirusList()

                # 콜백함수가 없으면 악성코드 목록을 뒤에 누적하여 리턴함!
                if isinstance(cb_fn, types.FunctionType):
                    cb_fn(inst.__module__, ret)
                
                if self.verbose:
                    print '    [-] %s.VirusList() :' % inst.__module__
            except AttributeError:
                continue
                
        return vlist



    def scan(self, filename, *callback):
        import FoxKernel

        #파일을 한개 씩 검사 요청할 경우 압축으로 인해 Self.update_info 데이터가 누적된 경우에..
        self.update_info = []
        scan_callback_fn = None

        move_master_file = False
        t_master_file = ''

        ret_vlaue = {
            'filename': '',
            'result': '',
            'virus_name': '',
            'virus_id': -1,
            'engine_id': -1
        }

        try:
            scan_callback_fn = callback[0]
            self.disinfect_callback_fn = callback[1]
            self.update_callback_fn = callback[2]
            self.quarantine_callback_fn = callback[3]
        except IndexError:
            pass

        file_info = FvcFile.FileStruct(filename)
        file_scan_list = [file_info]
    