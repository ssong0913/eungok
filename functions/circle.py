# 원의 둘레, 넓이 구하기
import math

def circle(r):
    radius = 2 * r * math.pi
    area = r**2 * math.pi
    print(f"반지름은 {r} 이고 원의 둘레는 {radius} 원의 넓이는 {area} 입니다.")    

r=int(input("반지름을 입력해주세요. : "))
circle(r) 