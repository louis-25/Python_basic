# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy"
str2 = "NiceMan"
str3 = ''

print(len(str1), len(str2), len(str3)) #문자열의 길이

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTap"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)


# 멀티라인
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'Niceman'

print(str_o1 * 10)
print(str_o2 + str_o3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77))
print(str(10.4))
print(str(77)+'a')

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

a = 'niceman'
b = 'orange'

print(a.islower()) # 소문자로 이루어졌는지
print(b.endswith('e')) # 끝나는단어 체크
print(a.capitalize()) # 첫글자를 대문자로
print(a.replace('nice', 'good')) # 대체
print(list(reversed(b)))

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(b[0:4:2])
print(b[1:-2])
print(b[:-1])