# print('qq')
# print('qq')
# 변수 : 데이터를 저장하기 위한 공간
# 변수 명 : 저장된 데이터를 접근하기 위한 이름
# =은 : 대입 연산자

# -----------------------------------------
# a=1.123
# print(a+3)
#
# a="z"
# print(a, 1)
# -----------------------------------------
# 사칙연산 : + - / * % //
# a=50
# b=3
# print('a+b=', a*b)
# print('a+b=', round(a/b,4))
# print('a/b=%.2f'%(a/b))
#
# print('a%b=', a%b)  #나머지
# print('a//b=', a//b) #몫
#
# a=10000
# b=3600
# c=60
# f=a%b/60
# print('시=', round(a//b))
# print('분=', round(a%b/60-1))
# print('초=', )

# 실습 )시,분,초 구하기
# s=10000
# t=s//3600
# print(t, '시간')
#
# r=s%3600
# m=r//60
# print(m, '분')
#
# s=r%60
# print(s, '초')

# 포멧 문자열
# 30+20=50
a=30
b=20
print(a,'+',b,'=',a+b)
print('%d + %d = %d' %(a,b,a+b))
print('%d - %d = %d' %(a,b,a-b))
print('%d / %d = %f' %(a,b,a/b))
print('%d * %d = %d' %(a,b,a*b))
# 소수점 조절 하고싶으면 사이에 소수점 갯수 설정
print('%d / %d = %.2f' %(a,b,a/b))
print('%d %% %d = %.2f' %(a,b,a%b))











