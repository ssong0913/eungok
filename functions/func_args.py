# 가변인자로 만드는 방법
# def hello_name(*args):
#     print(type(args))

def hello_name(*args):
    print(type(args))
    for name in args:
        print(f'{name}님 안녕하세요!!!')

# hello_name("김태경", "김태뽕", "김태뿡")

hello_name("오이", "오이1", "오이2", "오이3")

# 원하는 숫자를 나열하면 다 더하는 함수
def 함수(*args):
    num = 0
    for i in args:
        num = num + i
    return num
result = 함수(1, 5, 6, 4, 3, 100)
print(result)


""" def input_sum(*args): # input 은 내장함수(자체 기능이 있음)
    args = input("원하는 숫자를 , 를 기준으로 적어주세요!!!")
    num = 0
    for i in args:
        num = num + int(i)

    return num

data = input_sum()
print(data) """

