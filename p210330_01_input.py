# 사용장에게 입력받기
# 런 창에 입력을 하면 인풋 실행
# a=input('이름은')
# print('입력값', a)

# 실습) 나이를 입력받아 화면에 출력
# 입력한 값은 모두 문자 취급
# a=input('나이는?')
# print('나이는',a,'살', sep='') #sep 입력시 공백 변경 가능
# print('나이는',a,'살')
# print('나이는'+a+'살')

# txt='오늘의 날씨는'
# b=input('맑음, 흐림, 비옴')
# print('오늘의 날씨는', b, '입니다.')
# print(txt,b,sep='*')

# 도움말 출력
# help(print) #print 함수의 설명을 확인 가능

# 사용자가 입력한 값에 100을 더해 출력
# a=input('숫자는')
# a=int(a) #int는 정수로 변환해서 반환해줌
# a=float(a) #float는 실수(정수 포함)로 변환해서 반환해줌
# print(a+100)

# 실습)사용자에게 두 수를 입력받아 사칙연산 프로그램을 만들어 보세요.
# a=input()
# a=float(a)
# b=input()
# b=float(b)
# print(a,'+',b,'은',a+b,sep='')
# print(a,'-',b,'은',a-b,sep='')
# print(a,'*',b,'은',a*b,sep='')
# print(a,'/',b,'은',a/b,sep='')
# ------------------------------------------------------------
# a=int(input('첫번째 수'))
# b=int(input('두번째 수'))
# print('%d + %d = %d' %(a,b,a+b))
# print('%d / %d = %.2f' %(a,b,a/b))
# --------------------------------------------------------------
# d=input('두수는?')
# a=int(d.split()[0])
# b=int(d.split()[1])
# print(a+b)
#
# d=input('두수는?').split()
# a,b=map(int,d) #map은 d의 각 값을 int함수를 적용한 후 a,b에 대입
# print(a, b)


#실습) 반지름을 사용자로 부터 입력 받아 원의 넓이를 구해 봅시다 (원주율 :3.14)
# 반지름의 길이는 = 5
# 원의 넓이는 78.5 이다
# a=float(input('하나'))
# b=float(input('둘'))
# print('원의 넓이는',a*b)

# 해석) 원의 넓이를 구하시오
# r=float(input('반지름'))
# print('원의 넓이는',r*r*3.14) #78.5
# print('원의 넓이는',r**2*3.14) #78.5








