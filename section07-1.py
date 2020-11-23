# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네이스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
# 클래스 선언
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
print(user1.name) # Kim
user1.user_info_p()

user2 = UserInfo("Park")
print(user2.name) # Park
user2.user_info_p()

print(user1.__dict__) # 네임스페이스 출력
print(user2.__dict__)

# 예제2
# self의 이해
# self가 부여되면 인스턴스를 생성하여 호출 가능
# self가 없으면 클래스를 직접 호출하여 사용해야함
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print('function2 called!')
    
self_test = SelfTest()
# self_test.function1 # 호출안됨
SelfTest.function1() # 호출됨
self_test.function2() # 호출됨

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    # 클래스 변수는 공유되기 때문에 인스턴스가 생성될때마다 영향 받는다
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Lee')
user3 = WareHouse('Park')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

# 인스턴스는 자신의 네임스페이스에 변수가 없으면 클래스에서 변수를 찾는다

print(user1.stock_num)
