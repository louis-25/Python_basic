# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999
big_int2 = 888888888888888888888888888888
f1 = 1.234
f2 = 5.678
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7)) #절대값
n, m = divmod(100, 8) #몫은 n 나머지는 m으로 들어감
print(n, m)

import math
print(math.ceil(5.1)) # 5.1보다 크면서 가장 작은 정수
print(math.floor(5.1)) # 5.1보다 작으면서 가장 큰 정수


