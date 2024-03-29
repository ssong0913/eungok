import argparse
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

def circle_square_round(a):
    square = a*a*math.pi
    round = 2*a*math.pi
    return square, round

def pasing_argument():    
    parser = argparse.ArgumentParser(
        description='Process some Arguments Parsing',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # positional arguments
    parser.add_argument(
        'title', 
        metavar = '문자열',
        type = str,
        help = "write your messege at positional arguments"
    )

    parser.add_argument(
        'number', 
        metavar = '숫자',
        nargs='+',
        type = float,
        help = "이차방정식의 계수를 정할 숫자"
    )

    args = parser.parse_args()
    print(args)
    return args

def main():
    args = pasing_argument()
    if args.title == "1":
        square, round = circle_square_round(args.number[0])
        print(f'넓이 = {square}, 둘레의 길이 = {round}')
    elif args.title == "2":
        quadratic_equation_roots(args.number[0], args.number[1], args.number[2])

main()