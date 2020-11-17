# Section04-3
# 파이썬 데이터 타입 (자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)

# 선언방법
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1]) # 110

print(e[2][1]) # Banana
print(e[-1][-2]) # Banana

# 슬라이싱
print(d[0:1]) # 10
print(d[0:2]) # 10, 100
print(e[2][1:3]) # Banana, Orange

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c'] # 리스트가 통째로 들어갈 수 있음
print(c)

del c[1] #리스트 요소 삭제
print(c)
del c[-1]
print(c)

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 마지막에 원소 추가
print(y)
y.sort() # 크기 순서대로 정렬
print(y)
y.reverse() # 원소를 거꾸로 정렬
print(y)
y.insert(2, 7) # 2번 인덱스에 7추가
print(y)
y.remove(2) # 원소 2를 찾아삭제
print(y)
y.pop() # 맨 마지막에 있는 원소를 꺼낸다
print(y)
ex = [88, 77]
# y.append(ex) # 리스트를 통째로 추가
y.extend(ex) # 리스트의 원소를 추가
print(y)

# 삭제 : del, remove, pop

# 튜플 (순서o, 중복o, 수정x, 삭제x)
# 프로그램에 영향을 끼치는 중요한 key값을 다루기에 적합

# 튜플선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2] # 튜플은 삭제가 안됨
print(c[2])
print(c[3])
print(d[2][2]) # c

print(d[2:]) # a, b, c
print(d[2][0:2]) # a, b

print(c + d)
print(c * 3)

# 튜플 함수

z = (5, 2, 1, 3, 1)

print(z)
print(3 in z) # 원소 3이 z에 있는가?
print(z.index(5)) # 원소 5가 몇번째 인덱스에 있는가 -> 0
print(z.count(1)) # z에 원소 1이 몇개나 있는지
