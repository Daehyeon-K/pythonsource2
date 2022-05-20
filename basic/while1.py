# 반복문 (while)
# 역시 블록을 안쓰니, indentation으로 사용
# 1 ~ 10 출력

i = 1 # 초기화
while i<11 : # 조건
    print(i, end=" ")
    i+=1 # 증감

print()

# 1 ~ 100 짝수 출력
i = 1
while i < 101:
    if(i%2==0):
        print(i, end=" ")
    i+=1

print()

# 1 ~ 100 홀수 출력
i = 1
while i < 101:
    if(i%2==1):
        print(i, end=" ")
    i+=1

print()

# 1 ~ 100 합계 출력
i = 1
sum1 = 0
while i < 101:
    sum1 += i
    i+=1
print(sum1)

# sum() 함수
# range() 함수
print(sum(range(1,101)))

# 구구단 출력
i = 1
while i<10:
    j = 1
    print("{}단 : ".format(i), end="")
    while j<10:
        print("%3d" % (i*j),end="")
        j += 1
    i += 1
    print()