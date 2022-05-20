# 연산자
# 산술연산자 : +, -, *, /(실수), //(몫), %(나머지), **(제곱)
a, b = 5, 3
print(a+b, a-b,a*b, a/b, a//b, a%b, a**b)

print()
s1, s2, s3 = "100", "100.123", "999999999"
print(s1+s2+s3) # 연결 의미로 + 쓰임 100100.123999999999
print(float(s1)+float(s2)+float(s3))
#print(s1+1) # TypeError: can only concatenate str (not "int") to str

# 복합대입연산자 : +=, -+, *=, /=, //=, %=, **=
a = 10
a += 5
print("a : ",a)
a -= 5
print("a : ",a)
a *= 5
print("a : ",a)
a /= 5
print("a : ",a)
a //= 5
print("a : ",a)
a %= 5
print("a : ",a)
a **= 5
print("a : ",a)
print()

# 실습 : 777,777원
# 화폐 교환 5만원권, 1만원권, 5천원권, 1천원권 몇 장 씩
a=777777
print("5만원권:{}장, 1만원권:{}장, 5천원권:{}장, 1천원권:{}장, 나머지:{}원".format(a//50000,a%50000//10000,a%50000%10000//5000,a%50000%10000%5000//1000,a%50000%10000%5000%1000))

b=777777
b50k=b//50000
b%=50000
b10k=b//10000
b%=10000
b5k=b//5000
b%=5000
b1k=b//1000
b%=1000

# 관계연산자 : ==, !=, >=, <=, <, >
a, b = 10, 0
print(a==b, a!=b, a>=b, a<=b, a>b, a<b)

# 논리연산자 : and, or, not
print(100 > 60 and 60 > 15)
print(100 > 60 or 60 < 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(! True) 자바처럼 ! 이걸로 못함. not으로

# 비트연산자 (&, |, ^, ~, <<, >>)
print(10 & 7) # 2
print(10 | 7) # 15
print((100 > 60) & (60 > 15))
