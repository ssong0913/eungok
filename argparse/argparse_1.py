import argparse
import math
import numpy as np


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

    """ args = parser.parse_args()

    print(args)
    print(f'지금 수업은 {args.title}입니다.') """


    parser.add_argument(
        'radius', 
        metavar = '숫자',
        type = int,
        help = "write radius of circle"
    )
    args = parser.parse_args()

    return args


def main():
    args = pasing_argument()
    print('지금 실행하는 코드는 argparse 기초 1 입니다.')
    print(f'원의 반지름을 옵션으로 받아서 {args.title}를 구합니다')
    square, round = circle_square_round(args.radius)
    print(f'넓이 = {square}, 둘레의 길이 = {round}')

main()