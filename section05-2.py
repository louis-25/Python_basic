# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is : ", v2)

for v3 in range(1,11):
    print("v3 is : ", v3)

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 까지의 합 : ', sum1)
print('1 ~ 100 까지의 합 : ', sum(range(1, 101)))
print('1 ~ 100 까지의 합 : ', sum(range(1, 101, 2))) # 1부터 100까지 2개씩 건너뛰면서 합한다

# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for name in names:
    print("You are : ",name)

word = "dreams"

for s in word:
    print("Word : ", s)

my_info = {
    "name" : "Kim",
    "age" : 33,
    "city" : "Seoul"
}

for key in my_info:
    print("my_info", key) # 기본값인  key값이 출력된다

for key in my_info.values():
    print("my_info", key)

for key in my_info.keys():
    print("my_info", key)

for key in my_info.items(): # 키 & 값 둘다 출력
    print("my_info", key)

name = "KennRY"

#대문자는 소문자, 소문자는 대문자로 출력
for n in name:
    if n.isupper():
        print(n.lower(), end="")
    else:
        print(n.upper(), end="")

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")

# for - else 구문 (반복문이 정상적으로 수행된 경우 else블럭 수행)
for num in numbers:
    if num == 33:
        print("found : 33!")
        break    
else:
    print("Not found 33.....")

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))