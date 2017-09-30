# New Opensource Vaccine, FoxVc.  

## Warning  
**1.2.7버전 이하의 FoxVC은 가능하면 사용하지 마십시오.**  
악성코드 탐지 안정성에 문제가 있습니다.   
되도록이면 **1.2.8버전 이상의 FoxVc**을 추천합니다.(1.2.6은 권장될 수 있습니다.)  

**Do not use FoxVC versions below 1.2.7 if possible.**     
There is a problem with malware detection stability.   
We recommend **FoxVc version 1.2.8 or later.**    


## HI, Im noob Opensource Program coder, Nicht.

+ This Program is follwing GNU/GPL Ver.3, so **anyone can modificate this program on own system environment.**  
+ **This program was created with Python 2.7,**  
**Reqirement Libs are [hashlib, os, sys, logging, datetime, time, Win32com(pywin32)].**    
+ **This Vc only support Signature-based malware detection.**  
+ **Im trying to implement heuristic analysis using Python 2.7, However, I expect that it will take a considerable amount of time to realize it because there is not a lot of research data, and there is no case left for data by implementing heuristic inspection using Python.**    
+ Malware DB -> main.mdb, main.hdb || These will be updated continuously as soon as possible.  
**I made new Server at 2017-09-25, for Malware_analysis. New Server is consists of [Cuckoo SandBox, Maltrieve, Yara_Generator, guest OS(Win7 or Ie8XP)]**  


## New Informations for Update:
  
  ### 1. FoxVc Ver 1.2.8 >> [Successefully updated on 2017-09-16 AM.12:24]   
  && New Version[1.2.8] will be updated on ** [Succesefully updated on 2017-09-18 FM.5:12] &&**  
  1. Maleware Database "sort module" is updated.  
    >> "File_Hash_List" Type is modificated.  
      >> I removed newline characters for stabilize malware detection.  
   2. New Cure Module is created.  
        >> You can choose remove or neglect malware, with malware's installed_Directory_path.  
          >>
        
  ### 1-1. FoxVc Ver 1.2.81 >> New update files will be uploaded on 2017-10-.
          
  1. Malware detections for Windows drive!  
    >> upport malware detection for windows system files!  
    >> dministrator permission requesting function is updated!  
  2. Logging_Level is updated! (Info, Warning, critical, error)
        
         
  ### 2. FoxVc Ver 1.2.9 >> [Successefully updated on 2017-09-24 PM.4:53] 
  **1. Support Various Operating System -> Linux, Unix environment.**    
        >> Linux, Unix root permission requesting function is updated.[new function]  
        >> Already tested on Ubuntu 16.04LTS  
        >> Testing on OpenBSD, Solalis at imao.  
          **New Supporting OSs are :**  
           
            > + Ubuntu 16.04.1 LTS-i386,EM64T  
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
              + Element OS-i386,EM64T**     

### A TEST HAS ALREADY BEEN COMPLETED IN UBUNTU, CENTOS, OPENBSD, SOLALIS, KALI, BT.  
  **TESTING ON TAILS, ELEMENT, SUSE AT IMAO.**    
  
  # Warning          
  **This scripts are unstable. so i upload various beta scripts after 1.2.9, like 1.2.91, 1.2.92, 1.2.93 ~  
  So, You can see the newly modified source code in the "Test Code for Linux ver" folder before the stable FoxVc 1.2.9 version is uploaded.** 

  ### [INFO] Malware Database is updated!  
  **&& New malware DB will be updated on 2017-10-&&**  
  1. Currently Variant malwares are updated!  
  2. New Function will start supporting!  
     >> Cloud-Based ASD(Anlab Smart Defence) Analysis.  
     >> ASD cloud automatic malware analysis system.  
        >> This service structure is a new analytical technique developed by anlab to respond to new and variant malwares.    
                
  
  
### 3. FoxVc Ver 1.3.0 >> [Successefully updated on 2017-09-30 AM:2:23] 
**&&This version supperted not only python 2 users but also python 3 users! &&**  
1. New functions are supported!  
   >> The source code has been updated to make Python users more than 2 versions available through grammatical modifications.  
 
        
### 4. FoxVc Ver 1.3.1 >> New update files will be uploaded on 2017-10-    
**&& This version supports "Updated-UI" for easier checking and handling resulted-malwares. &&**  
**1. UI update -> focusing on checking resulted-malwares.**  
     >> It take forms like string list return-type.  
**2. New function supported.**  
     >> New version of Cure module.    
            
### 5. FoxVc Ver 1.3.2 >> New update files will be uploaded on 2017-10-.  
**&& This version supports "Admin management UI". &&**   
1. Ui will be updated for administrator.  
   >> Admin Permission must be needed.
    >> New Function(Admin permission request is updated)
      >> The Execute Windows Permission Request window will appear on the screen.
            
### 6. FoxVc Ver 1.3.3 >> New update files will be uploaded on 2017-10-.  
**&& This version supports "Html page for checking and management malware's md5_hash, size, directory_path." &&**      
1. New function will be supported.  
    >> This function is focusing on malware analysis for System manager.  
    >> Html page for checking and management malwares md5_hash, size, directory_path.  
      >> Page will be made html, you can check  malwares name, md5_hash, installed_malware_directory_path, link for connect to https://www.virustotal.com/  
            
            
            
            
## All new notifications and informations.  
+ **관리방식 교체로 인해 기존 저장소를 삭제하고 동일이름의 새로운 저장소로 업그레이드 되었습니다.**  
+ 시험기간과 가족여행의 병행으로 현 시점(2017-09-29)부터 10월 11일까지 새로운 버전 업로드가 일시중단 됩니다.  다만 이미 배포된 파일의 관리와 사이트 유지보수는 지속적으로 시행될 예정입니다. 새로운 1.3.0 버전은 09-30에 업로드될 예정입니다. 당연히 1.3.0 버전은 원할히 실행되지 않을 않을 것입니다.  고로, lib2to3를 사용한 스크립트로 1.3.01 버전으로 새로개발된 스크립트가 2017-10-02일에 업로드될 예정입니다.
+ 안정화된 윈도우버전은 pyinstaller를 통해 exe파일로 압축되며, 안정된 리눅스/유닉스버전은 sh파일로 압축될 예정입니다.  
+ planning to supporting new function, Virtual dynamic analysis(Heuristic). :D  
     
Soure of Image : https://www.boredpanda.com/fox-species-wildlife-photography/  
 
## This Document made by Nicht, using "Markdown Language" 

## Informations of Coder    
 
 Email : miho0_0@naver.com  
 youtube : anonymous0korea0@gmail.com  
 Lee Joon Sung; Republic of Korea, Seoul, Gangnam, Gaepodong.  
 
