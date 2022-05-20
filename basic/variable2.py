# 변수 - 타입이 없음
# str, int, float, bool

# 문자형 - "", '' 모두 허용
str1 = "Life is too short, You need Python"
str2 = 'Life is too short, You need Python'
str3 = """ 
Life is too short, You need Python

 """
str4 = ''' 
Life is too short, You need Python
 '''

print(str1)
print(str2)
print(str3)
print(str4)

# + : 문자열 연결
head = "Python"
tail = " is fun"
print(head+tail)

# * : 문자열 반복
a = "Python"
print(a * 2)
print("*"*50)
print("My Program")
print("*"*50)

# 문자열 인덱싱 (왼쪽 기준 0, 맨 뒤가 -1 - 오른쪽 기준 -1)
str1 = "Life is too short"
print("str1[3] : ",str1[3]) # e
print("str1[-3] : ",str1[-3]) # o
print()
# 마지막 숫자 범위 포함 안하고 -1한 인덱스 까지
print("str1[0:4]",str1[0:4])
print("str1[4:8]",str1[4:8])
print("str1[9:]",str1[9:])
print("str1[:17]",str1[:17])
print("str1[0:-4]",str1[0:-4])

# 실습
str2 = "20220520Sunny"
# date 변수에 날짜만 담기
date = str2[:8]

# weather 변수에 날씨만 담기
weather = str2[8:]

# 둘 다 출력
print(date,weather)

# date 변수에 있는 값을 2022-05-20 출력
print(date[:4],date[4:6],date[6:], sep="-")

# date, weather 출력 (2022-05-20 Sunny)
print("{}-{}-{} {}".format(date[:4],date[4:6],date[6:],weather))

# 세번째 인자는 인덱스 증가 수 (디폴트는 1)
print("str1[-1::-1]",str1[-1::-1])
print("str1[0:4:2]",str1[0:4:2])
print("str1[0:8:3]",str1[0:8:3])
print("str1[4:0:-2]",str1[4:0:-2])

# 문자열 관련 함수들
# len(str) : 문자열 길이
print("문자열 길이", len(str1))
# count('c') : 문자열에 포함된 특정 문자의 수
print("문자열에 포함된 특정 문자의 수 :",str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : %d" % str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : {}".format(str1.count('t')))
#find(str) : 특정 문자 시작 첫 위치
print("특정 문자가 시작되는 첫 위치 반환",str1.find("i"))
print("특정 문자가 시작되는 첫 위치 반환",str1.find("k")) # 없으면 -1
print("특정 문자가 시작되는 첫 위치 반환",str1.find("i", 4)) # 4 이후 첫 위치
#index() : find와 역할은 같지만, 차이는 없는 문자 찾을 때 에러가 나는지 -1 반환하는지 차이
print("특정 문자가 시작되는 첫 위치 반환 index",str1.index("i"))
# print("특정 문자가 시작되는 첫 위치 반환 index",str1.index("k")) #ValueError: substring not found
#startswith(), endswith() : ~로 시작하는지, ~로 끝나는지 (return bool, case sensitive)
print(str1.startswith("L")) # True
print(str1.startswith("l")) # False
print(str1.endswith("T")) # False
print(str1.endswith("t")) # True
print()
#join() : 삽입
a = " , "
print(a.join("abcde")) # a , b , c , d , e
print()
# upper() / lower() : 대소문자 변경
a = "abcde"
print("소문자를 대문자로 변경",a.upper())
a = "ABCDE"
print("대문자를 소문자로 변경",a.lower())
# swapcase() : 대소문자 서로 변경
a = "Python is Easy"
print("대소문자 상호변환",a.swapcase())
# title() : 두문 대문자
print("python Is Easy".title())

# 문자열 비교
print("abc" == "ABC")

# 공백 제거
# strip(), lstrip(), rstrip()
a = "    hi    "
print(a.strip()) # 양측 공백 제거
print(a.lstrip()) # 좌측 공백 제거
print(a.rstrip()) # 우측 공백 제거
print()
# replace() : 문자열 바꾸기
print(str1.replace("Life", "Your leg"))
print()
# split() : 문자열 나누기 -> 나눠서 리스트로 리턴 (배열 아님)
print(str1.split()) # ['Life', 'is', 'too', 'short']
a = "a:b:C:D"
print(a.split(":")) # ['a', 'b', 'C', 'D']
print(str1.splitlines()) # 줄바꿈 기준으로 나누기
a = "하나\n둘\n셋"
print(a.splitlines()) # ['하나', '둘', '셋']

# 문자열 구성 파악
print("1234".isdigit())
print("abcd".isalpha())
print("abcd1234".isalnum())
print("abcd".islower())
print("ABCD".isupper())

# 실습 : URL 기준 암호 생성
# http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2 : 처음 만나는 . 이후 부분은 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 문자 개수 + !로 구성
# 결과 예시 : nav51!
a = "http://naver.com"
a = a.split("/")[2].split(".")[0]
# password = a[:3]+len(a)+a.count('e')+"!" # TypeError: can only concatenate str (not "int") to str
# => 파이썬은 자동 형 변환 안해줌 : 문자 + 숫자 연결 안됨
password = a[:3]+str(len(a))+str(a.count('e'))+"!"
print(password)

