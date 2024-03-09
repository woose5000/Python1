a = 10 
def b():
    return 10
class C:
    pass

class Circle:
    def __init__(self,반지름):
        self.__pi = 3.14
        self.__반지름 = 반지름
    def 넓이(self):
        return self.__pi * (self.__반지름 ** 2)

    def 둘레(self):
        return 2 * self.__pi*self.__반지름