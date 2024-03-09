# (1) 프로그래밍 언어의 기본 문법
# (2-1) Algorithm 문제풀이
# 알고리즘 문제 풀이 
# (2-2) 모듈 공부
# 인공지능, 데이터 분석, 웹 개발 

import os 

script_path = os.path.abspath(__file__) # 파일의 절대 경로 구하기 
print(script_path)

script_dir = os.path.dirname(script_path) # 파일의 direct name
print(script_dir)

os.chdir(script_dir) # 디렉토리 변경

output = os.listdir(".")
print(os.getcwd())
print("os.listdir()", output)
print()

# 과거의 알고리즘 문제 
## 과거 : 퀵소트를 구현해라, 머지소트를 구현해라 
## 현대 
## - 미로를 탈출하는 방법을 구하라.
## - 최적의 엘리베이터 공식을 구해라.
## - 미국 전역으로 바이러스가 퍼지는 시간을 구해라 
## - 폴더라면 또 탐색하기 라는 재귀적 구성으로 현재폴더에 있는 모든 파일을 탐색하기

def read_folder(path):
    # 폴더의 요소 읽어들이기
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path + "/" + item)
        else:
            print("파일:", item)

read_folder(".")