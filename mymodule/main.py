import hellomodule

print(hellomodule.a, hellomodule.b, hellomodule.C)

# 모듈을 활용하면 관심사를 기반으로 함수, 변수, 클래스 등을 모을 수 있습니다. 
# 실제 코드 실행 흐름을 굉장히 단순하게 만들 수 있음. 

a = hellomodule.Circle(10)

print(a.넓이(),a.둘레())
