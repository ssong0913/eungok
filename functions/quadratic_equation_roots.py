# 이차방정식 해 구하기
import math
def quadratic_equation_roots(a, b, c):
    if b**2 - 4*a*c < 0:
        print(f'실근이 없습니다.')
    else:
        x = b**2 - 4*a*c
        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)
    
        if x == 0:
            print(f'방정식의 해는 중근 {x1} 입니다.')
        else :
            print(f'x1 = {x1} or x2 = {x2}')

a = int(input("이차항의 계수 : "))
b = int(input("일차항의 계수 : "))
c = int(input("상수항의 계수 : "))

quadratic_equation_roots(a, b, c)
