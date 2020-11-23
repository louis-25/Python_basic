# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법
# NameError : 참조변수 없음
# ZeroDivisionError : 0 나누기 에러
# IndexError : 인덱스 범위 오버
# KeyError : 없는키 조회 -> get함수 이용하면됨
# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# ValueError : 참조 값이 없을 때 발생
# TypeError : 형변환 잘못한 경우

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValuedError!')
else:
    print('Ok! else!') # 예외가 발생하지 않은경우


# 예제2

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred ValuedError!')
else:
    print('Ok! else!') # 예외가 발생하지 않은경우


# 예제3
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValuedError!')
else:
    print('Ok! else!') # 예외가 발생하지 않은경우 (정상실행된 경우)
finally:
    print('finally') # 예외가 발생하거나 말거나 무조건 실행

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok finally')


# 예제5
# 예측 가능한 예외 조건을 여러개 설정가능
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValuedError!')
except IndexError:
    print('Not found it! - Occurred ValuedError!')
except Exception:
    print('Not found it! - Occurred ValuedError!')
else:
    print('Ok! else!') # 예외가 발생하지 않은경우 (정상실행된 경우)
finally:
    print('finally') # 예외가 발생하거나 말거나 무조건 실행

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError # 고의로 에러를 발생시킴
except ValueError:
    print('문제 발생!')
except Exception as e:
    print(e) # 에러의 내용을 출력
else:
    print('Ok!')