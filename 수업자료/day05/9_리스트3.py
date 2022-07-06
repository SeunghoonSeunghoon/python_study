# 리스트를 저장한 변수는 '참조형 변수'라고 한다

li1 = [10,20,30,40,50]

li2 = li1           # 참조형 변수를 대입하면, 가리키는 대상의 위치를 복사
                    # 이를, 얕은 복사라고 한다
print(f"li1 = {li1}, li2 = {li2}")

li2[3] = 400
print(f"li1 = {li1}, li2 = {li2}")


li3 = li1[:]        # 슬라이싱을 해서 복사하면, 실제 데이터가 복사된다
                    # 이를, 깊은 복사라고 한다
li3[3] = 40
print(f"li1 = {li1}, li3 = {li3}")
