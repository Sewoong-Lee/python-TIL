#리스트:연속적인 메모리의 할당
d=[10,20,30,40,50]
print(d)
print(d[0])
print(d[1:3]) #출력시 대괄호[] 가 있으면 리스트 형태이다.
print(d[0],d[2])

# 리스트 안의 변수 변환
d[1]=200
print(d[1])

# d[5]=200 인덱스 초과
d.append(500) #추가 방법
print(d)

d.insert(10,400) #중간 추가
print(d)

d=['홍길',20,165.5]
print(d[0])

c=[['q',1],['w',2]]
print(c[1][0])







