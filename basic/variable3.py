# 변수
# type(var) : 타입 확인

a = 3.5 
print(type(a)) # <class 'float'>

b = True # True, False 대문자로 시작
print(type(b)) # <class 'bool'>

c = 123
print(type(c)) # <class 'int'> 

d = "123"
print(type(d)) # <class 'str'> 


# 형 변환 기능 : str(), int(), float(), bool()
# 가능 여부 확인
print()
print(str(True),type(str(True))) # "True"
print(str(1),type(str(1))) # "1"
print(str(98.6),type(str(98.6))) # "98.6"
print()
print(int(True),type(int(True))) # 1
print(int(False),type(int(False))) # 0
print(int("1"),type(int("1"))) # 1
print(int(98.6),type(int(98.6))) # 98
#print(int("98.6"),type(int("98.6"))) # ValueError: invalid literal for int() with base 10: '98.6'
# 아예 정수이거나 실수인 경우만 가능. 실수 모양의 문자는 안바꿔줌
print()
print(float(True),type(float(True))) # 1.0
print(float(False),type(float(False))) # 0.0
print(float("1"),type(float("1"))) # 1.0
print(float(98),type(float(98))) # 98.0
print()
print(bool(0),type(bool(0))) # False
print(bool(-1),type(bool(-1))) # True
print(bool(1),type(bool(1))) # True
print(bool("1"),type(bool("1"))) # True
print(bool(98),type(bool(98))) # True
print(bool(98.26),type(bool(98.26))) # True

