# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서X, 중복x, 수정o, 삭제o

# Key : Value (Json) -> MongoDB
# 선언

a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 960703}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name')) # get을 붙이면 안전하게 조회할 수 있다
print(a.get('address'))

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3)
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values()) #보통 이렇게 안쓰고 list로 형변환하여 사용
print(list(a.values())) 

print(list(a.items())) # 튜플형태로 반환
print(1 in b)
print('name' in a)
print('name' not in a)

# 집합 (Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

# 형변환
t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# s1과 s2교집합
print(s1.intersection(s2)) 
print(s1 & s2)

#합집합
print(s1.union(s2)) 
print(s1 | s2)

#차집합
print(s1.difference(s2)) 
print(s1 - s2)

print('집합 추가 & 제거')
# 집합 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18) # 추가

print(s3)

s3.remove(15) # 제거
print(s3)

print(type(s3))