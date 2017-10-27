# New Opensource Vaccine, FoxVc.  

* * *

## Warning  
**1.2.7버전 이하의 FoxVC은 가능하면 사용하지 마십시오.**  
악성코드 탐지 안정성에 문제가 있습니다.   
되도록이면 **1.2.8버전 이상의 FoxVc**을 추천합니다.(1.2.6은 권장될 수 있습니다.)  

**Do not use FoxVC versions below 1.2.7 if possible.**     
There is a problem with malware detection stability.   
We recommend **FoxVc version 1.2.8 or later.** 

* * *

## HI, Im noob Opensource Program coder, Nicht.

+ This Program is follwing GNU/General Public License 3, so **anyone can modificate this program on own system environment.**  
+ **This program was created with Python 2.7** 
+ This Vc only support Signature-based malware detection.  
+ **Im trying to implement heuristic analysis using Python 2.7, However, I expect that it will take a considerable amount of time to realize it because there is not a lot of research data, and there is no case left for data by implementing heuristic inspection using Python.**    
+ Malware DB -> main.mdb, main.hdb || These will be updated continuously as soon as possible.  
**I made new Server at 2017-09-25, for Malware_analysis. New Server is consists of [Cuckoo SandBox, Maltrieve, Yara_Generator, guest OS(IE8 Win7)]**  



* * *

## All new notifications and informations.  

+ **관리방식 교체로 인해 기존 저장소를 삭제하고 동일이름의 새로운 저장소로 업그레이드 되었습니다.**    
>- **새로운 버전인 N_FoxVC 이 개발중에 있습니다.**  
> **N_FoxVc의 테스트 코드는 TestCode폴더에서 각 업데이트별로 확인할 수 있습니다**  

Soure of Image : https://www.boredpanda.com/fox-species-wildlife-photography/   


* * *  
* * *

## New Informations for updates!  


### 새로이 개발중인 N_FoxVc에 적용된 기술과 기능에 대한 설명.  
개발중인 N_FoxVc은 기존 FoxVc의 문제점을 패치하고 있습니다.  

* 기존에 존재했던 문제점은...  
``` 


1. 악성코드 검사후 각 malware별 치료 모듈이 확고하지 않았음.  
   -> 커널이 파일을 불러와 이를 플러그인 엔진에게 진단/치료 가능한지 질의하고 명령을 하달하는 플러그인 구조 사용하여 재구축

2. 백신 엔진이 직접 악성코드를 탐지하는 형태라서 악성코드 분석시, 상당히 시간이 걸림  
   -> 커널이 사용자가 입력한 파일/디렉토리를 파악하여(파일의 open을 최소화 시키기 위함), 이를 각 모듈에 질의 하는 방식으로
      검사속도를 상당히 감소시킴.
      
3. Anti-Virus 프로젝트 파일 미성숙  
   -> 백신 프로젝트 폴더의 구조 및 구성의 미성숙.
      확고한 폴더와 파일을 구축하고, 각 백신 플러그인 엔진을 커널이 무결성검증 검사를 통해 관리상 용이점 .
      
4. 각종 취약점에 대응하는 보안기술 미적용  
   -> 백신 커널, 플러그인 엔진, 악성코드DB, 악성코드 패턴, 코어파일등 중요한 파일에 대해 위.변조 방지기법 채용
   
        1. Header : 백신 이니셜 + 정보 표시[lastest updated files](날짜, 시간값)
        2. Body : individual Key를 이용해 암호화된 RC4키 + RC4로 암호화된 압축된 내부 소스코드
        3. Tailer : 개인키로 암호화한 Header와 Body전체에 대해 md5를 3번 연산한 결과.
    -> 이와 같이 소스코드는 py -> pyc -> fxm의 파일변환을 거치며 암호화되어 해커가 백신코어나 파일을 임의로 변조하여 적용할 수 없도록..
        
5. 정규화되지 않은 소스코드들  
   -> 소스코드 내 변수, 함수명, 파일명등을 사용하기 쉽도록 재명하고, 최대한 정규표현식을 사용하여 구축함.

6. malwareDB로부터 나오는 악성코드 패턴을 효율적으로 사용하지 못하는 소스코드 
   -> 기존 malware-DB에서 추출한 데이터를 리스트로 나누어 사용하는 방식을 대폭 업그레이드함.


``` 

[!] 이를 보완하여 상당히 확고화된 새로운 백신을 개발하였습니다.  
    아직도 개발중이긴하지만, 미완성인 Test-code가 2017년-10-28일 오후에 업로드 됩니다.  
    
    
* * *
  

## 1. FoxVc Ver 1.2.8 >> [Successefully updated on 2017-09-16 AM.12:24]   
&& New Version[1.2.8] will be updated on ** [Succesefully updated on 2017-09-18 FM.5:12] &&**  
1. Maleware Database "sort module" is updated.  
>- "File_Hash_List" Type is modificated.  
> I removed newline characters for stabilize malware detection.  
  
2. New Cure Module is created.  
  >- You can choose remove or neglect malware, with malware's installed_Directory_path.   

* * *

## 1-1. FoxVc Ver 1.2.81 >> New update files will be uploaded on 2017-10-.
1. Malware detections for Windows drive!  
>- upport malware detection for windows system files!  
>- dministrator permission requesting function is updated!  
2. Logging_Level is updated! (Info, Warning, critical, error)

## 1-2. FoxVc Ver 1.2.82 >> It will be uploaded on 2010-10-23
1. More Reliably Updated Administrator Rights Request Function

* * *

## 2. FoxVc Ver 1.2.9 >> [Successefully updated on 2017-09-24 PM.4:53] 
**1. Support Various Operating Systems -> Linux, Unix environment.**    
>- Linux, Unix root permission requesting function is updated.[new function]  
> [INFO] Already tested on Ubuntu 16.04LTS  
>- Testing on OpenBSD, Solalis at imao.  
```    

      [!] New Supporting Operating Systems are :  
            >
              + Ubuntu 16.04.1 LTS-i386,EM64T  
              + Ubuntu 16.04.1 Server-i386,EM64T  
              + Ubuntu 12-i386,EM64T  
              + CentOS-Testing  
              + OpenBSD-i386,EM64T  
              + OpenSuSe-i386,EM64T  
              + Kali Linux2.0-i386,EM64T  
              + Kali Linus1.1.0-i386,EM64T  
              + BackTrack 5 R3-amd64  
              + BackTrack 5 R3-x32  
              + Tails OS-i386,EM64T  
              + Element OS-i386,EM64T  
              + OpenSolalis EM64T
              
``` 

### A TEST HAS ALREADY BEEN COMPLETED IN UBUNTU, CENTOS, OPENBSD, SOLALIS, KALI, BT.  
**TESTING ON TAILS, ELEMENT, SUSE AT IMAO.**    
  
# Warning          
**This scripts are unstable. so i upload various beta scripts after 1.2.9, like 1.2.91, 1.2.92, 1.2.93 ~  
So, You can see the newly modified source code in the "Test Code for Linux ver" folder before the stable FoxVc 1.2.9 version is uploaded.**  

* * *

## [INFO] Malware Database is updated!    
**1. Currently Variant malware's data are updated!**  
2. New Function will start supporting!  
  >- Cloud-Based ASD(Anlab Smart Defence) Analysis.  
  > ASD cloud automatic malware analysis system.  
  > This service structure is a new analytical technique developed by anlab to respond to new and variant malwares.    
                
* * *
  
## 3. FoxVc Ver 1.3.0 >> [Successefully updated on 2017-09-30 AM:2:23] 
**&&This version supperted not only python 2 users but also python 3 users! &&**  
1. New functions are supported!  
  >- The source code has been updated to make Python users more than 2 versions available through grammatical modifications.  
  > The original version uses sys.version_info to scan the installed version of Python on your system and import and use optimized code for each version.  
2. branch version uses Lib2to3 to build python2 versions of FoxVc and python3 versions of FoxVc separately.  


# 4. A new FoxVc is developed!!!  
## The N_FoxVc is built with a structure and methodology that is significantly different from existing FoxVcs!  
1. N_FoxVc is will be uploaded on 2010-10-30  
  >- New Functions are updated!  
  > supporting zip and rar, 7zip, tar, tar.gz, tar.bz, bz files.  
2. Introduced a new type of vaccine engine!  
  - The structure of the FoxVc engine is based on the "Structure and Principle of Anti-Virus" written by professor Choi Won-hyuk, who is currently developing Kikom vaccine.
 



## Information of Coder    
 
- Email : miho0_0@naver.com  
- youtube : anonymous0korea0@gmail.com  
- Lee Joon Sung; Republic of Korea, Seoul, Gangnam, Gaepodong.  

### Help noob open source developer with your mercy! ~~( Angela Ziegler )~~  
+ Donate : 986b71b9-d74b-464d-82c7-6b20c1ea576b
> (Donalbe cryptocurrency Tpyes are BTC, XMR, ETH, XDN, BCN, FCN, XDN, INF8, AEON)  
