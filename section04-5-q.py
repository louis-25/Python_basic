# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
print("1번문제")
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print('1. q1길이: ', len(q1))
print()
# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("2번문제")
print('apple;orange;banana;lemon')
print()
# 3. 화면에 * 기호 100개를 표시하세요.
print("3번문제")
for i in range(100):
    print('*',end='')

print('*' * 100)

print()
# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
print("4번문제")
a = "30"
print(int(a))
print(float(a))
print(complex(a))
print(a)
print()
# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
print("5번문제")
print('Niceman'[-3:])

q5 = "Niceman"
print(q5[4:7])

q5_idx = q5.index("man")
print(q5_idx)
print(q5[q5_idx : q5_idx+3])
print()
# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
print("6번문제")
q6 = "Strawberry"

print(list(reversed(q6)))
print(q6[::-1])
print()
# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
print("7번문제")
q7 = "010-7777-9999"

print(q7[0:3]+q7[4:8]+q7[9:13]) # 수작업

print(q7.replace('-', '')) # replace

#정규 표현식
import re
print(re.sub('[^0-9]','',q7)) #숫자를 제외한 나머지를 공백으로 바꾼다
print()
# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
print("8번문제")
q8 = "http://naver.com"

print(q8[7:])
print(q8.replace("http://",""))
print()
# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
print("9번문제")
print("NiceMan".upper())
print("NiceMan".lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
print("10번문제")
q10 = "abcdefghijklmn"
print(q10[2:5])
print(re.sub('[^cde]','',q10))
print()
# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
print("11번문제")
q11 = ["Banana", "Apple", "Orange"]
q11.remove("Apple")
print(q11)
print()

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
print("12번문제")
q12 = (1, 2, 3, 4)
print(list(q12))
print()

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
print("13번문제")
q13 = {
    "성인" : 100000,
    "청소년" : 70000,
    "아동" : 30000    
}
print(q13)
print()
# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
print("14번문제")
q13["소아"] = 0
print(q13)
print()

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print("15번문제")
print(list(q13.keys()))
print()

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print("16번문제")
print(list(q13.values()))
print()

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
