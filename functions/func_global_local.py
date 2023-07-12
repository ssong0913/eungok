# Global & Local
a = 3
b = 5
def local_variable(): #로컬(지역) 변수 a,b는 함수 안에서만 사용 가능
    a = 5
    b = 4
    a = a + b
    print(a)

print(a)

def local_variable(): # global 전역변수
    global a
    b = 4
    a = a + b
    print(a)

def local_variable_error():
    print(b)

local_variable_error()

local_variable()

