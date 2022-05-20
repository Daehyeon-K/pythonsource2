# format

# format() : 중괄호로 위치를 잡고, 나중에 삽입
# print("{}".format())

print("{} and {}".format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print()
print("{var1} and {var2}".format(var1='You',var2='Me'))
print("I ate {number} apples. So I was sick for {day} days".format(number=10,day=3))
print("I ate {0} apples. So I was sick for {day} days".format(10,day=3))
# 아래 형태로 포맷값을 사용하려면 키 값을 꼭 같이 넣어줘야 함
print("Test1 : {0:5d}, Price : {1:4.2f}".format(776,6534.123))
print("Test1 : {a:5d}, Price : {b:4.2f}".format(a=776,b=6534.123))
