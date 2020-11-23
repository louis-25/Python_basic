# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
# code

# 함수 호출
# 함수명(prameter)

# 함수 선언 위치 중요!

# 예제1
def hello(world):
    print("Hello", world)

hello("Python!")
hello("world!")

# 예제2
def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("Python!!!")
print(str)

# 예제3 (다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(1)
print(val1, val2, val3)

# 예제3-2 (데이터 반환타입)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(1)
print(lt)

# 예제4 가변인자 (* - 튜플 , ** - 딕셔너리)
# *args

def args_func(*args): # 매개변수의 제한을 받지않는다
    #print(args)
    for i, v in enumerate(args): # 인덱스를 생성해준다
        print(i, v)

args_func('kim')
args_func('kim', 'Lee')
args_func('kim', 'Lee', 'Park')

# **kwargs
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1='Kim', name2='Park', name3='Lee')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'kim', 'lee', age1=12, age2=22)

# 예제5 중첩함수(클로저)
# 메모리를 효율적으로 관리할 수 있다

def nested_func(num):
    def func_in_func(num):
        print(num) # 3
    print("in func") # 1
    func_in_func(num + 10000) # 2

nested_func(10000)

# 예제6 (hint)
def func_mul3(x : int) -> list: # int형을 입력받아서 list로 반환을 명시적으로 알려준다
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10 # 변수에 함수 할당
print(type(var_func))

print(var_func(10))

# 람다
lambda_mul_10 = lambda num : num * 10 

print('>>>',lambda_mul_10(10))

def func_final(x, y, func): # 매개변수로 함수로 받을 수 있다
    print(x * y * func(10)) 

func_final(10, 10, lambda_mul_10) # 함수를 인자로 전달

print(func_final(10, 10, lambda x : x * 1000)) # 즉시 람다식을 인자로 전달가능
