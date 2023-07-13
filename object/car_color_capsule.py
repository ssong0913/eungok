class Car:

    def __init__(self, name, price, color):
        self.__name = name
        self.__price = price
        if price <= 100000000:
            raise ValueError('차값이 1억보다 커야 합니다.')
        self.__color = color

    def __str__(self):
        return (f'Car(name = {self.__name} , 가격 = {self.__price}, color = {self.__color})')

    @property # @=>데코레이터
    def color(self):
        return self.__color

    @color.setter # property 의 age
    def setColor(self, color):
        if self.__color == "노랑":
            raise ValueError('노랑은 안돼요!!')
        self.__color = color

car = Car("자전거", 1100000000,"파랑")
print(car)
print("======================")
# cat.age = 12
# cat.age(10)
car.setColor="Black"
# car.price = 1000000000
# print(car)
print(car.color)
