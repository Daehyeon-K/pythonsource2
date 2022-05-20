# 조건문 if
# 파이썬은 블럭(중괄호)을 사용하지 않고 들여쓰기로 구분

# if True:
#    print("True")

# a = 200
# if a < 100:
#     print("a는 100보다 작다.")
# elif a == 100:
#     print("a는 100과 같다.")
# else :
#     print("a는 100보다 크다.")

# if a > 100 and a<=200:
#     print("a는 100보다 크고 200보다 작거나 같다")
# elif 0 < a <= 100:
#     print("a는 0보다 크고 100과 같거나 작다")

# 실습 : 가장 큰 수 출력
a,b,c=12,6,18
if a <= b:
    if b <= c:
        print("가장 큰 수 : ",c)
    else :
        print("가장 큰 수 : ",b)
elif a > b:
    if a <= c:
        print("가장 큰 수 : ",c)
    else :
        print("가장 큰 수 : ",a)

print()

# if ~ else
if True:
    print("True")
else:
    print("False")

a = 55
if a < 100:
    print("a는 100보다 작다")
else :
    print("a는 100보다 크거나 같다")

print()

# 관계연산자, 논리연산자 함께
score,grade=90,"A"
if score >= 90 and grade == "A":
    print("합격")
else :
    print("불합격")

# 실습
# 숫자를 입력받아 짝홀 판단
# num = int(input("수 입력 >>"))
# if num%2 == 0:
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")
print()

# 현재 시간 기준으로 오전 오후 확인
import datetime
now = datetime.datetime.now()
day1 = ""
print(now)
print()
if now.hour>=12:
    day1="오후"
    print("{}년 {}월 {}일 {} {}시 {}분 {}초".format(now.year, now.month, now.day, day1 ,now.hour, now.minute, now.second))
else :
    day1="오전"
    print("{}년 {}월 {}일 {} {}시 {}분 {}초".format(now.year, now.month, now.day, day1 ,now.hour, now.minute, now.second))

print("오전" if now.hour < 12 else "오후")

# 삼항연산자
str = "안녕하세요" if True else "반갑습니다."
print(str)

# 중첩 if문
a = 75
if a > 50:
    if a < 100:
        print("a는 50보다 크고 100보다 작다")
    else:
        print("a는 50보다 크고 100보다 크거나 같다")
else:
    print("a는 50보다 작거나 같다")

# 다중 if (if ~ elif ~ else)
num = 90
if num >=90:
    print("A grade ", num)
elif num >= 80:
    print("B grade ", num)
elif num >= 70:
    print("C grade ", num)
elif num >= 60:
    print("D grade ", num)
else:
    print("F grade ", num)

print()
age,height = 27,180

if age >= 20:
    if height >= 170:
        print('A 지망 가능')
    elif height >= 160:
        print('B 지망 가능')
    else :
        print('지원 불가')
else :
    print("20세 이상 지원 가능")

# 실습
# 사용자에게 점수 입력받고 학점 출력
# > 80 A, > 60 B, > 40 C, > 20 D, > 0 F
grade = int(input("학점을 입력하세요 >> "))
print("학점 >> ", end='')
if grade > 80:
    print("A")
elif grade > 60:
    print("B")
elif grade > 40:
    print("C")
elif grade > 20:
    print("D")
else:
    print("F")


# 사칙계산기
# 사용자에게 숫자 두개, 연산자 입력받고 연산해 결과 출력
# 연산자는 +, -, *, /,43 %, //, **
a = int(input("첫 수를 입력하세요 >>"))
op = input("연산자를 입력하세요 >>")
b = int(input("둘째 수를 입력하세요 >>"))

print("결과 >> ", end='')
if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '%':
    print(a%b)
elif op == '//':
    print(a//b)
elif op == '**':
    print(a**b)