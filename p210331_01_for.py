#반복문 :for

# d=[1,2,3,4,5]
# for x in d: #범위인 d의 갯수만큼만 실행
#     print('python')

# d=['짱구','유리','철수']
# # for x in d:
# #     print(x)
#
# for x in [0,1,2]:
#     print(d[x])

#실습) 0부터 9까지 출력
# d=[0,1,2,3,4,5,6,7,8,9]
# for x in d:
#     print(x)

#range라는 함수는 (스타트값,스탑,건너뛸수)로 구성 (정수만 생성)
# print(list(range(10,50,2)))

# for x in range(1,10,2):
#     print(x)

#합계를 구하라
# s=0 #합계를 저장할 변수
# for x in range(1,11):
#     s=x+s
#     # print(s) #들여쓰기 되어 있으면 반복하라는 뜻임
# print(s)

# s=0
# for x in range(1,11):
#     s+=x #s=s+x
# print(s)

# 실습) 사용자가 몇까지 더할지 입력을 받아 결과를 구하시오
# a=int(input('시작'))
# b=int(input('마지막'))
# s=0
# for x in range(a,b+1,1):
#     s+=x
# print(s)

# 실습)1부터 100까지 더하다가 100까지의 합이 2000이 넘을때의 수를 출력하라.
# s=0
# for x in range(1,101):
#     s+=x
#     if s>2000:
#         break #반복문을 종료할때 사용하는 키워드
#
# print('x=',x,'s=',s)

#실습) 바보라는 글자가 발견되면 강퇴
# d=['안녕', '반가워', '하이', '바']
# b=['바보', '멍청이']
# for x in d:
#     print(x)
#     if x in b:
#         print('강퇴')
#         break
# else: #포문(반복문이) 정상수행 했다면, 브레이크가 안되었다면
#     print('당신은 바른말 사용자')

#continue : 계속 진행 (진행하던게 잘못되었으면 다시 돌아가 진행)
# d=[3,8,5,1,7,2,9]
# for x in d:
#     if x%2==1:continue
#     print(x)

#어떤 학생의 점수 리스트가 주어졌을떄 모든 학생의 점수가 60점이 넘으면 합격하는 프로그램을 작성하시오
#예) 점수리스트 [65,45,95,55,70]  [68,78,96,86,72]

# a=[65,45,95,55,70]
# b=[68,78,96,86,72]
#
# for x in b:
#     # print(x)
#     if x<60:
#         print('불합격')
#         break
# else:
#     print('합격')



# d=input('점수는?').split()
# d=map(int, d)
# # print(list(d))
# for x in d:
#     # print(x)
#     if x<60:
#         print('불합격')
#         break
# else:
#     print('합격')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 합계가 300점 이상이면 합격
a=[65,45,95,55,70]
b=[68,00,6,86,72]
s=0
for x in b:
    s += x
    if s>300:
        print('합격')
        break
else:
    print('불합격')

d=[100,100,100,55,70]
s=0
for x in d:
    s =+ x
    if s<300:
        print('합')
        break
else:
    print('불')


#set : 중복 데이터 허용 불가
# asia = {'한국','중국','일본'}
# asia.add('베트남')
# asia.add('중국')
# asia.remove('일본')
# asia.update({'한국','홍콩','태국'})
# print(asia)






























