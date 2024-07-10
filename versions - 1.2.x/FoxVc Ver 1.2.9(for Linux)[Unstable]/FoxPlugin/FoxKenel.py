# Author : github.com/miho030

# 상태
not_found = 0 # 악성코드가 없음 -> 찾지 못함
infected = 1 #감염되었음.
suspect = 2 #감염 의심.
warning = 3 #경고


# 악성코드 치료 방법 3가지

IGNORE = 0 # 파일을 그대로 냅둠.
PACK = 1 # 최상위 파일 압축
DELETE = 2 # 최상위 파일을 지움.
