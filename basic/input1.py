# 입력 : input()

# msg = input()
# print(msg)

# msg = input("이름 입력 : ")
# print(msg)

# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))
# print(num1 + num2) # casting 안하면 4555, 즉 입력 받으면 그 상태는 일단 str

# 실습
# 사용자에게 연/월/일 형태로 입력받고, 10년 후 날짜 출력
date = input("연/월/일 입력 >> ")
dateList=date.split("/")
print("입력한 날짜의 10년 후 >> {}년 {}월 {}일".format(int(dateList[0])+10,dateList[1],dateList[2]))