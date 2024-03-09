a = 10 
def b():
    return 10
class C:
    pass

class Circle:
    def __init__(self,반지름):
        if 반지름<0:
            raise ValueError()
        self.__pi = 3.14
        self.__반지름 = 반지름
    def 넓이(self):
        return self.__pi * (self.__반지름 ** 2)

    def 둘레(self):
        return 2 * self.__pi*self.__반지름
    
print("#hellomodule.py")
print(__name__)

if __name__ == "__main__":
    print("# 넓이()를 검증합니다.")
    if Circle(10).넓이() - 314 < 10 ** -7:
        print("넓이() 검증을 성공했습니다!")
    else :
        print("넓이() 검증을 실패했습니다!")
    print("#둘레()를 검증합니다.")
    if Circle(10).둘레() - 62.8 < 10 ** -7:
        print("넓이() 검증을 성공했습니다:success")
    else: 
        print("넓이() 검증을 실패했습니다:fail")