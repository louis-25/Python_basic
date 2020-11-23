# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print("----------------------------------------")

# 예제2
# with문은 따로 close를 선언해주지 않아도됨
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c)

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content)

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline() #한줄씩 읽어오기
    while line:
        print(line, end=' ')
        line = f.readline()

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' ********* ')
print()
# 예제7
score = []
with open('./resource/score.txt', 'r') as f:    
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2 
with open('./resource/text1.txt', 'a') as f: # 파일에 추가하기
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6): # 0 ~ 5
        f.write(str(randint(1, 45)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n','Lee\n', 'Park\n']
    f.writelines(list) # list의 내용을 한줄씩 파일에 쓴다

# 예제5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contests1!', file=f) # 파일에 print문으로 출력
    print('Test Contests2!', file=f)