# 표준 입출력 : 키보드나 화면을 통해서 사람과 컴퓨터가 데이터를 주고 받는 방식을 의미

# 표준 출력문 : print(), 화면에 정보를 출력한다
# 표준 입력문 : input(), 키보드를 통해서 데이터를 입력 받는다

n = input("정수를 입력해 주세요 :")

print("n =", n)
print(f"n의 타입 : {type(n)}")
# input()은 입력 받은 데이터를 '문자열'로 가져온다

n1 = input("\n정수1 : ")
n2 = input("정수2 : ")

print(f"n1 = {n1}, n2 = {n2}")
print(f"n1 + n2 = {n1 + n2}")