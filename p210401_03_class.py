#class 객체를 만들기 위한 툴 (램에서 독립적인 공간을 가지는)

class Car:
    #속성 : 필드라고 부름
    name='덤프트럭'
    color='노랑'
    pw=false
    #기능 :메소드
    def power(self):
        pw=not Car.pw
#대문자로 해야 구별 가능 (대문자는 객채를 만들기 위한거구나아~)
c1=Car()
print(c1.name)



