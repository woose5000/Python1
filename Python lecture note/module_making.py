# 모듈
# 파일 또는 폴더를 구성 

# import 모듈이름
# 현재 실행하고 있는 위치에서 "모듈이름"이라는
# 파일 또는 폴더가 있는지 확인
# (존재하지 않는다면) 환경 변수가 등록되어있는 위치에서 확인
import os
import sys
import math
# 따라서 존재한다면 오류가 발생한다. 

print(sys.path) # 환경변수 