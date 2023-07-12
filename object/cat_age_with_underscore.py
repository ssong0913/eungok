# 캡슐화 (외부에서 변형하는것 방지)
class Cat:
    def __init__(self, name, age):
        self.__name  = name #__로 캡슐화. 외부에서 변형하는것 방지
        self.__age = age

    def __str__(self):
        return f'Cat(name={self.__name}, age={self.__age}살)'
    
nabi = Cat("나비", 10)
nero = Cat("네로", 20)
    
print(nabi)
# print(nero)
print("===========================")

nabi.__age = 100
print(nabi)

