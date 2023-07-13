import argparse

class Car:
    def __init__(self, door_number, color, brand):
        self.door_number = door_number
        self.color = color
        self.brand = brand
    
    def __str__(self):
        return f'Car(door_number={self.door_number}, color={self.color}, brand={self.brand})'
    
    def lotto(self):
        print(f'문이 {self.door_number}개 이고, 색깔이 {self.color}인 {self.brand} 브랜드 차가 있습니다')

def pasing_argument():

    parser = argparse.ArgumentParser(
        description="Sample for using argparse",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        '-n',
        '--number',
        metavar="차도어",
        nargs="*",
        type=int,
        help="assign function option",
        default=[4]
    )
    parser.add_argument(
        '-c',
        '--car',
        metavar="자동차",
        type=str,
        nargs="*",
        help="assign function option",
        default=["흰색","벤츠"]
    )

    args = parser.parse_args()
    print(args)
    return args

def main():
    args = pasing_argument()
    car = Car(args.number[0],args.car[0],args.car[1] )
    car.lotto()

main()