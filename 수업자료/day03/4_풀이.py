# 조건연산자가 아닌 조건문으로 푼다

# 1. 정수를 입력 받아서 절대값을 출력
n = int(input("정수 입력 :"))

if n < 0 :
    n = -n
print (f"절대값은 {n}입니다~")

# 2. 두 정수를 입력 받아서 큰 수를 출력
# 단, 같은 경우는 '같다'라고 출력한다
n1 = int(input("입력1"))
n2 = int(input("입력2"))

if n1 > n2 == 0 :
    print(f"큰 수는 n1 = {n1} 입니다")   
elif n1 < n2 :
    print(f"큰 수는 n2 = {n2} 입니다")
else :
    print("두 수는 같습니다")

# 3. 정수를 입력 받아서 3과 7의 공배수이면 출력
n = int(input("\n3. 3, 7 공배수 :"))

if n % 3 == 0 and n % 7 == 0 :
    print("공배수 맞음")
else :
    print("공배수 아님")


# 4. 세 정수를 입력 받아서 가장 큰 수와 가장 작은 수를 출력
# - 최대, 최소를 의미

x1 = int(input("입력1 :"))
x2 = int(input("입력2 :"))
x3 = int(input("입력3 :"))
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
if x1 > x2 :
    if x1> x3:
        print (f"{x1}")
    elif x2 > x3:
        print (f"{x3}")
    else :
        print (f"{x2}")
if x2 > x3 :
    if x2> x1:
        print (f"{x2}")
    elif x1 > x3:
        print (f"{x3}")
    else :
        print (f"{x1}")
if x3 > x1 :
    if x3> x2:
        print (f"{x3}")
    elif x1 > x2:
        print (f"{x1}")
    else :
        print (f"{x2}")
