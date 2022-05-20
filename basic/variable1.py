# 변수 - 타입이 없음
# str, int, float, bool

# 숫자형 : 정수, 실수, 8진수, 16진수 등
a = 13
print(a," = ",type(a))

a = -7
print(a," = ",type(a))

a = 0
print(a," = ",type(a))

a = 1.2
print(a," = ",type(a))

a = 0o177 # 8진수
print(a," = ",type(a))

a = 0x8fff # 16진수
print(a," = ",type(a))


# 사칙연산
# a = 3; b = 4
a, b = 3, 4
print (a + b)
print (a / b) # 정수 나눗셈 아님, 계산 결과 실수 범위로 보여줌 0.75
print (a // b) # 나눈 몫 0 (정수 나눗셈)
print (a % b) # 나눈 나머지 3
print (a ** b) # a의 b제곱 3^4 = 81
