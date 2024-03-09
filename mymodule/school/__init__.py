if __name__!="__main__":
    from .student import *
    from .studentlist import *
else:
    from student import *
    from studentlist import *

a = "모듈입니다."
def b():
    print("school 모듈입니다.")

c = Student(10)
d = StudentList()

d.append("학생")
c.sum()

print(d)
print(c)