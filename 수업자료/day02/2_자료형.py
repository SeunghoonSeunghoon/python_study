# 자료형(=Data Type) 프로그램에서 사용되는 데이터의 타입을 의미

# 1. 문자열 : 따옴표로 묶인 데이터, 단어나 문장을 표현하는 데이터
# 2. 정수 : 따옴표가 없는 숫자 데이터. 연산을 위한 데이터
# 3. 실수 : 숫자 중에서 . (소수점)이 포함된 데이터
# 4. 논리 : 참/거짓을 판별하기 위한 데이터

print("10")
print(10)
print(10.0)
print()              # 빈 Print()문은 줄바꿈을 생성하기 위한 용도로 사용되기도 한다


print("10" + "20")   # 문자열의 덧셈은 파이썬에 '이어붙이기'가 된다
print(10 + 20)
print(10 + 3.14)
print()

# 자료형을 확인하는 키워드가 있다
print(type("10")) #str : string, 문자열을 의미
print(type(10))   #int : integer, 정수를 의미
print(type(10.0)) #float : float, 실수를 의미


