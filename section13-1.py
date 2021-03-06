# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

words = [] # 영어 단어 리스트(1000개 로드)

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip()) # 리스트에 추가
    
print(words) # 단어 리스트 확인

input('Ready? Press Enter Key!') # 사용자의 키보드 입력을 대기받음

start = time.time() # 시작시간 체크

while n <= 5: # 문제의 개수
    random.shuffle(words) # 리스트의 요소를 랜덤으로 섞어줌
    q = random.choice(words) # 아무값이나 랜덤으로 하나 뽑음

    print()

    print('Question # {}'.format(n))
    print(q) # 문제 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():
        print('Pass!')
        cor_cnt += 1
    else:
        print('Wrong!')

    n += 1

end = time.time() # 종료시간 체크
et = end - start
et = format(et, '.3f') # 소수점 3자리까지 표기

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# 게임 시간 출력
print('게임 시간 : ', et, '초', '정갑 개수 : {}'.format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass