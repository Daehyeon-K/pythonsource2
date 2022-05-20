# 반복문 (for ~ )
# for 변수 in 범위

# print(range(5)) # range(0, 5)
# print(list(range(5))) # [0, 1, 2, 3, 4]
# print(list(range(1,5))) # [1, 2, 3, 4]   
# print(list(range(0,10,2))) # [0, 2, 4, 6, 8]
# print(list(range(50,1,-2))) # [50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# # 0 ~ 9 출력
# for i in range(10):
#     print(i,end=" ")
# print()
# # 1 ~ 10 출력
# for i in range(1,11):
#     print(i,end=" ")
# print()
# # 1 ~ 100 출력
# for i in range(1, 101):
#     print(i,end=" ")
# print()
# # 1 ~ 100 홀수 추력
# for i in range(1,101):
#     if i%2==1 : print(i,end=" ")
# print()
# 1 ~ 100 합계
# sum1=0
# for i in range(1,101):
#     sum1+=i
# print(sum1)

# 실습 : 숫자 하나 입력받고, 1부터 입력값까지 합계 구해 출력
# num = int(input("숫자 입력 >> "))
# sum1=0
# for i in range(1,num+1):
#     sum1 += i
# print(sum1)

# for문 없이 합
# print(sum(range(1,num+1)))

# 문자열 출력
word = "dreams"
for i in word:
    print(i)

# 이중 for 문
for i in range(3):
    for j in range(3):
        print(j,end=" ")
    print()

# 구구단 2 ~ 9단
for i in range(2,10):
    if i == 2 : 
        print("구구단", end="")
        for j in range(2,10):
            print("%3d단" % (j),end="")
        print()
    print("{}단 : ".format(i), end="")
    for j in range(1,10):
        print("%4d" % (i*j),end="")
    print()

# break, continue
i = 1
while i <= 10:
    if i==5:break
    print(i,end=" ")
    i+=1

i = 1
print()
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

# 실습 : 1 ~ 10 출력, i가 5면 출력 x
print()
for i in range(1,11):
    if i==5: continue
    print(i, end=" ")
print()
