#내장함수
#sum
# d=[5,8,9,6,2]

#기존은 아래와 같이 했음
# s=0
# for x in d:
#     s+=x
#     print(s)

#썸 사용시 편함
# print(sum(d))

#사용자 함수로 썸 구현 #사용자 함수의 정의
# 매개 변수는 리스트 / 반환값은 합계
# def mysum(a): #def 는 디파인(정의한다) 만들 함수의 이름은 알아서, 반드시 뒤에 괄호가 들어온다 / 안에 무조건 매개변수가 있어야 변환 가능
#     s=0
#     for x in a:
#         s += x
#     #print(s)
#     return s
#
# d=[5,8,9,6,2]
# r = mysum(d)
# print('리턴값',r)

#내장함수 max, min
# d=[5,18,4,6]
# m=max(d)
# print('가장 큰 값',m)
#
# mi=min(d)
# print('가장 작은 값',mi)

#max 구현 **********************이거 다시 봐바************************
# def mymex(d):
#     mx=0
#     for x in d:
#         if x>mx:
#             mx = x
#     return mx
#
#
# a=[5,18,4,6]
# print(mymex(a))
# a=[55,18,4,6]
# print(mymex(a))


# min 함수 구현
#)내가 한거
# def mymin(a):
#     mi=float('inf')
#     for x in a:
#         if x<mi:
#             mi=x
#     return mi
#
# c=[5,18,4,8]
# print(mymin(c))
#
# #2)선생님 풀이
# def mymin(md):
#     mi = md[0]
#     for x in md:
#         if x<mi:
#             mi=x
#     return mi
#
# c = [5, 18, 4, 8]
# f=mymin(c)
# print(f)

#ord 함수
#한글은 유니코드 체계
# print(ord('!'),len('!'))
# print(ord('가'),len('가'),'가'.encode(),len('가'.encode()))

# a=chr(65)
# print(a)

#실습1) 두 수를 입력받아 사칙 연산을 하는 함수
# 매개변수 2수
#반환값:결과

#
# def add(a,b):
#     return (a+b)
#
# def ss(a,b):
#     return (a-b)
#
# print(add(10,20))
# print(ss(10,20))


#실습) 월급 구하기
#년봉,시급,초과근무시간을 매개변수로 받아 월급을 계산하고 반환하는 함수
#(월급 = 년봉 / 12 + 시급*초과근무시간)

#내가 한거   \\\\\\\\\\\\\\\\\\\\\\\\\\\이거 다시 ㄱㄱ\\\\\\\\\\\\\\\\\\
# def s(a,b,c):  #함수 내에 인풋하는건 안좋은거랭
#     a=int(input('연봉'))
#     b=int(input('시급'))
#     c = int(input('초과근무시간'))
#     return a/(12+b*c)
# print(s(0,0,0))

#풀이
# def sl(a,b,c):
#     return a/12+b*c
#
# y=int(input('연봉'))
# t=int(input('시급'))
# o=int(input('초과'))
# # n=sl(y,t,o)
# print(sl(y,t,o))





































