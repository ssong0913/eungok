# argparse 활용
# object->str_cats.py

import argparse

class Cat:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound
    
    def __str__(self):
        return f'Cat(name={self.name}, color={self.color}, sound={self.sound})'
    
    def lotto(self):
        print(f'이름은 {self.name}이고, 색깔은 {self.color}의 고양이가, {self.sound}라고 웁니다')

def pasing_argument():

    parser = argparse.ArgumentParser(
        description="Sample for using argparse",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        '-c',
        '--cat',
        metavar="cat",
        type=str,
        nargs="*",
        help="assign function option",
        default=["나비","흰색","야옹"]
    )

    args = parser.parse_args()
    print(args)
    return args

def main():
    args = pasing_argument()
    # print(f'이름은 {args.cat[0]}이고, 색깔은 {args.cat[1]}의 고양이가, {args.cat[2]}라고 웁니다')
    cat = Cat(args.cat[0],args.cat[1],args.cat[2] )
    cat.lotto()

main()
    

""" nabi = Cat("나비", "흰색")
nero = Cat("네로", "검은색")

print(nabi)
print(nero) """