# +=======================================================================================+
# 사용자 시스템에 설치되어 있는 파이썬의 버전을 감지하고 각 버전에 최적화된 모듈 임포트함.
# +=======================================================================================+

# 파이썬 버전에 따라 버전에 최적화된 모듈을 실행하는 부분
# sys모듈을 사용하여 설치된 파이썬 버전을 변수로 지정.
# FoxVc을 실행하는 시스템에 파이썬 2버전 이상이 설치된경우.
if FoxPyver[:1] == 2:
    print "[+] ", "You have Python2 !", "Start python 2 modules..\n"
    FoxVcpy2()
else:
    # FoxVc을 실행하는 시스템에 파이썬 3버전 이상이 설치된경우.
    if FoxPyver[:1] == 3:
        print ("[+] ", "You have Python3 !", "Start python 3 modules..\n")
        FoxVcpy3()
    else:
        print (" ")
        print ("+==========================================================================+")
        print ("[ - Warning - ] Our FoxVc does not support less than the Python 2 version.")
        print ("[-] For smooth execution, please install Python version 2 or version 3.")
        print ("+==========================================================================+")