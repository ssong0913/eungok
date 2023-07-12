class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __str__(self): # str 은 고정
        return f'Cat(name={self.name}, color={self.color})'
    
    def lotto(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}, 야옹~~야~옹~~')

nabi = Cat("나비", "흰색")
nero = Cat("네로", "검은색")

# 인스턴스를 호출하면 문자열 str이 고정되어 나옴
print(nabi)
print(nero)