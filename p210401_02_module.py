# 모듈

# import time
# time.localtime()
# print(list(time.localtime()))
# print(time.localtime().tm_year,'년')
# print(time.localtime().tm_mon,'월')
# print(time.localtime().tm_mday,'일')
# print(time.localtime().tm_hour,'시')
# print(time.localtime().tm_min,'분')

#
# from _datetime import datetime
# new=datetime.now()
# print(new)
# print(new.strftime('%y-%m-%d %H-%M-%S'))


#sleep 함수 = 프로그램 속도 제어
# import time
# print('시작')
# time.sleep(3)
# print('끝')


#타이머 만들기

# a=0
# import time
# print('시작')
# while a<5:
#     a += 1
#     time.sleep(1)
#     print(a, '초')
#     if a > 5: break
# print('끝')


# import time
# sec=int(input('?'))
# print('시작')
# for x in range(1,sec+1):
#     time.sleep(1)
#     print(x,'초')
# print('끝')


# #아래처럼도 가능
# from time import sleep
# sec=int(input('?'))
# print('시작')
# for x in range(1,sec+1):
#     sleep(1)
#     print(x,'초')
# print('끝')

#랜덤 모듈
#주사위게임
# import random
# b=random.randint(1,6)#시작점과 끝부분
# print(b)


#주사위게임 만들기
# import random
# a=random.randint(1,6)
# b=random.randint(1,6)
# print('a',a,'b',b)
#
# if a>b:
#     print('a')
# elif b>a:
#     print('b')
# else:
#     print('무승부')


#3세판----------------------------이거 해보자----------------------------------------
# import random
# aw=0 #이긴 횟수
# bw=0
# while True:
#     a=random.randint(1,6)
#     b=random.randint(1,6)
#     print('a',a,'b',b)
#
#     if a>b:
#         print('a')
#     elif b>a:
#         print('b')
#     else:
#         print('무승부')

#sample 모듈 (한정된 제한 내에서 고르는것)
import random
# print(random.sample([1,2,3,4,5],3))
# print(random.sample(range(1,46),6))

#choice 중에 하나 골라주는거
# print(random.choice(['가위','바위','보']))

#suffle 섞는다. (기존의 데이터만 섞는다.)
# d=['가','가','나','나']
# random.shuffle(d)
# print(d)


#그래픽 모듈
# import turtle
# turtle.shape('turtle')
# turtle.color('red')
# for x in range(5):
#     turtle.forward(100)
#     turtle.right(70)
# turtle.done()





