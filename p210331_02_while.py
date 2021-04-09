#반복문
#조건이 참일 동안 실행
# while True:
#     print('py')

# a=0
# while True:
#     a += 1
#     if a>10:
#         break
#     print(a)
# #
# a=0
# while True:
#     a += 1
#     print(a)
#     if a>9: break
#
#
# #1부터 10까지 합을 출력
# s=0 # 합계를 누적할 변수
# a=0 #증가하는 변수
# while True:
#     a+=1
#     if a > 10: break
#     s+=a
#print(s)


# a=0
# while a<10:
#     a += 1
#     print(a)

#a가 증가 되면서 합계를 구하고 그 합이 2000이 넘으면 종료한다
# s=0 #합계 누적
# a=0 #증가 변수
# while s<2000:
#     a += 1
#     s += a
#     print(a,s)
#
# while True:
#     a += 1
#     s += a
#     if s>2000:
#         print(a,s)
#         break



#사용자가 입력한 수를 누적하다가 만약 0을 입력하면 누적합계를 출력 하겠다.
#1)
# s=0
# while True:
#     a = int(input('더할 값은?'))
#     if a==0: break
#     s+=a
# print(s)

#2)
s=0
a=-1
while a!=0:
    a = int(input('더할 값은?'))
    s+=a
print(s)

#다음과 같이 별을 찍어 보아라


