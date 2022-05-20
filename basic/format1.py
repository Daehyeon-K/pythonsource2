# format()
# 자바에서의 ~~.printf("%d", 3)와 같은 개념
# %c - 문자 하나, %f - 실수, %d - 정수, %s - 문자(사실 만능 숫자든 실수든)

# print('%d' % 100)
# print('%5d' % 100) # 5자리 맞춰서 출력 (숫자는 우측 정렬 기준)
# print('%05d' % 100) # 5자리 맞추고 숫자니 우측 정렬인데 빈 곳 0으로 채움
# print()
# print('%s' % "hi")
# print('%5s' % "hi")
# print()
# print("%8.2f" %12.21)
# print("%-8.2f" %12.21) # - 표시로 왼쪽 정렬
# print("%-8.2f" %12.2134567)
# print()
# print("I eat %d apples" % 3)
# print("I eat %s apples" % 3)
# number = 4
# print("I eat %s apples \n// type of number : " % number, type(number))
# print()
print("%d : %s" % (1, "홍길동"))
print("%d : %s - %f" % (2, "김성호", 93.2))
print("Test1 : %5d Price : %4.2f" % (776, 5634.123))
print()
print("I eat %s apples" % 3)
print("I eat %s apples" % 3.156)
print("I eat %s apples" % "3")
print()
print("Error is %d%%" % 98)