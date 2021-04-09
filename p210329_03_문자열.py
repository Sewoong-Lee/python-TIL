# 문자열

txt = 'python is easy'
print(txt)
print(txt[1])
print(txt[2:5])
print(txt[-1]) #뒤에서부터
print(txt[7:9])#스타트:스탑  (마지막껀 출력 안됨)
print(txt[:2])
print(txt[7:-1])
print(txt[-4:])#마지막 끝까지 출력

#s='my house' 가 있을 때 house 만 출력해라.
s='my house'
print(s[3:])
print(s[-5:])

txt = "012345678901234567890123456"
print(txt[:10])
print(txt[10:20])
print(txt[20:])