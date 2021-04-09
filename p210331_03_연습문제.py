#연습문제
#1) 별찍기
# print('*'*2)
# 별찍기1
for x in range(1,7):
    print('*'* x)

for x in range(1,10,2):
    print('*'* x)



# 별찍기2)
# for x in range(7,0,-1):
#
#     print('*'* x)
#
# 별찍기3) ******************** 이거 다시 해바야댐******************
# for x in range(6,0,-1):
#     for a in range(1,7,1):
#         print(' '* x, end=''); print('*'* a)

# for x in range(7,0,-1):
#     print(' ' * x,end='')
#     for a in range(1,7,1):
#         print('*'* a)



# 별찍기1)
# a=0
# while a<5:
#     a+=1
#     print('*'* a)

# 별찍기2)
# a=5
# while a>0:
#     a+=-1
#     print('*'* a)

# # 별찍기3)
# a=8
# s=0
# while a>0:
#     a+=-1
#     s+=1
#     print(' '* s, end=''); print('*'* a)


# 실습2) 구구단을 출력하는 프로그램을 만들어 보자
# 2*1=2 등등
# for x in range(1,10) :
#     print('2 *',x,'=',end=' '); print(2*x)
#
# a=int(input('수'))
# for x in range(1,10):
#     print(a,'*', x, '=', end=' '); print(a * x)

# 해석)
# for x in range(1,10) :
#     print('2 * %d = %d' %(x,2*x))

# a=int(input('단수'))
# for x in range(1,10) :
#     print('%d * %d = %d' %(a,x,a*x))

#*********************** 2중 반복문 구구단
# for x in range(2,10):
#     for y in range(1,10):
#         print('%d * %d = %d' %(x,y,x*y))


# 숫자를 입력받아 그 범위 안의 수 중 0부터 3의 증가수를 출력하는 프로그램을 만들어 봅시다
# 내가한거)
# a=int(input('첫수'))
# b=int(input('둘째수'))
# d=0
# c=0
# for x in range(a,b):
#     if x%2==0:
#         x=c
#     else:
#         x=d
#     print(d)

# 해석)
# 1번
# a=int(input('첫수'))
# # b=int(input('둘째수'))
# # for x in range(a,b+1,3):
# #     print(x, end=' ')
# 
# # 2) 3의 배수만
# for x in range(0,a+1):
#     if x%3==0:
#         print(x, end=' ')


#  2개의 수와 기호를 받아서 계산기 프로그램을 만들어보자
# 단, 사용자가 q를 입력하면 계산기 프로그램 종료 (이프와 와이로 제작 와일 유리)
# 1)두 수와 기호를 입력받는다
# 2)기호에 따라 계산
# 3)계속 진행여부 입력
#내가한거) 개망함
# a=0
# b=0
# c=기호
# q='q'
# q=input('종료')
# while True:
#     a=int(input('첫수'))
#     c = input('기호')
#     b=int(input('다음수'))
#     if c=='+':
#         a+b
#     if c=='-':
#         a-b
#     if c=='*':
#         a*b
#     if c=='/':
#         a/b
#         print()

# 풀이
# while True:
#     a=int(input('첫수'))
#     b=int(input('다음수'))
#     c=input('기호는?')
#     if c=='q':break
#     if c=='+':
#         print(a+b)
#     elif c=='-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         print(a/b)

# while True:
#     a=int(input('첫수'))
#     b=int(input('다음수'))
#     c=input('기호는?')
#     if c=='+':
#         print(a+b)
#     elif c=='-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')
#     if input('종료?')=='q': break

# while True:
#     a=input('첫수')
#     if a=='q': break
#     a=int(a)
#     b=int(input('다음수'))
#     c=input('기호는?')
#     if c=='+':
#         print(a+b)
#     elif c=='-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')

# 3) 기호를 잘못입력하면 무한반복하게
# while True:
#     a=input('첫수')
#     if a=='q': break
#     a=int(a)
#     b=int(input('다음수'))
#     while True: #원하는 기호가 언제 나올지 몰라 whil을 사용한거임
#         c=input('기호는?')
#         if c in ['+','-','*','/']:
#             break
#     if c=='+':
#         print(a+b)
#     elif c=='-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')

#반학생들의 점수가 딕셔너리로 저잘되어 있을때 값이 90점 이상인 학생들의 키만 출력하시오
# da={1:94,2:87,3:91,4:75,5:92}
# print(da.keys()) # 키만 가져옴 (1,2,3,4)
# print(da.values()) #값만 가져옴 (94,87,91,75,92)
# print(da.items()) #2개를 다 가져오기 위하여 사용
# 위 세개를 이용 가능

# for n,s in da.items(): # 점수의 1:94 를 2개로 나누어 변수에 넣음
#     if s >= 90:
#         print(n,'번')


# 6) 사원의 판매량 출력
# 1- 사원의 판매수량 입력
# 2- 히스토그램 그리기
# d=['홍길동','이순신','김순','철수'] -리스트를 작성하여도 가능
# q=[10,15,5,7] -리스트를 작성하여도 가능 (하지만 딕셔너리가 나음)
# 이렇게 데이터 구조를 잡을 예정 s={'홍길동':10,'이순신':15,'김순':5,'철수':7}
# d=['홍길동','이순신','김순','철수']
# q={} # 판매수량을 저장할 딕셔너리
# for n in d:
#     q[n]=int((input)(n + ':'))  ####### 이거 중요****************************************
# for x,y in q.items():
#     print(x,':','*'*y)
#
#
# #실습7) 적정체중 구하기
# d=['홍길동','이순신','김순','철수']
# q={}
# for n in d:





















