현 상황 FoxVc 프로젝트 구조

폴더 : -
파일 : ^
빈파일 : $$
추가 설명 : #

빈파일은 추후에 개발이 완료되는 시점으로 업데이트될 예정.

Structure of FoxVc Project!

- N_FoxVc
	- FoxDB
		^*.db
	- FoxEngine
		- FoxPlugins
		- FoxCore
			# 암호화 모듈(Encrypt Files)이 이곳으로 옮겨질 예정.
	- Tools	
		-Encryption
			- Decrypt
				$$
			- Encrypt
				^ FoxCrypt.py
				^ fxmKmd.py
				^ TestCode.py
				^ TestCode.fxm
			- RC4
				^ FvcRC4.py
				^ how to use FvcRV4.py
			- RSA
				^ FvcRSA.py
				^ FvcrsaK.py


현 진행 상황 : 

프로그램을 배포판으로 제작하여 사용할 때, 해커가 Anti-Virus의 커널, 플러그인 엔진의 작동 원리를 파악하고,
임의로 프로그램을 수정하지 못하게 하기 위한 모듈을 개발/구축하였음.

2017.11.03일에 Anti-Virus의 핵심인 백신 커널이 안정화 되어 업로드 될 예정임.

