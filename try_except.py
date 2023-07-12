# 예외처리
""" list_1 = []

numbers = list(range(10)) """

# try except로 사용하기
""" 
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드 """

# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print(y)
# except:    # 예외가 발생했을 때 실행됨
#     print('0으로 나누면 안돼!! 안돼!!')

# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print(y)
# except Exception as e:
#     print(f'error : {e}')

# try:
#     x = input('나눌 숫자를 입력하세요: ')
#     y = 10 + x
#     print(y)
# except Exception as e:
#     print(f'error : {e}')

def main():
    try:
        print("1")
        print("2")
        prin("3") # 에러
        print("4")
    except NameError as e:
        print("예외 발생! main ", e.args)
        print(e.__traceback__)
main()