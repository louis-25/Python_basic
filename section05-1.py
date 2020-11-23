# Section05-1
# 파이썬 흐름제어 (제어문)
# 조건문

print(type(True))
print(type(False))

# if문
if True:
    print("YES")

if False:
    print("NO")

# if-else문
if False:
    print("No")
else:
    print("Yes")

# 관계 연산자
# >, >=, <, <=, ==, !=

a = 10
b = 1

print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a >= b) # True
print(a < b) # False
print(a <= b) # False

# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = ""

if city:
    print("True")
else:
    print("False") # False출력

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and : ',a > b and b > c) # True
print('or : ',a > b or c > b) # True
print('not : ',not a > b) # True
print(not False) # True
print(not True) # False

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5 + 10 > 0 and not 7+3 == 10) # False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다")
else:
    print("불합격하셨습니다")

# 다중조건문 (if, elif, else)
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("num 등급 F", num)

# 중첩조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지원가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

