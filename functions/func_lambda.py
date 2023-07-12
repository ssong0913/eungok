# 람다 표현식에 조건부 표현식 사용하기

# lambda 매개변수들: 식1 if 조건식 else 식2
# 다음은 map을 사용하여 리스트 a에서 3의 배수를 문자열로 변환합니다. 
#map => map(함수, 리스트)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_data = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(list_data)
# 람다 표현식 안에서 조건부 표현식 if, else를 사용할 때는 :(콜론)을 붙이지 않습니다

# 람다 표현식 안에서는 elif를 사용할 수 없습니다. 
# 따라서 조건부 표현식은 
# 식1 if 조건식1 else 식2 if 조건식2 else 식3 
# 형식처럼 if를 연속으로 사용해야 합니다.
list_data_1 = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(list_data_1)
                    # 1이면 str(1), 아니면 else-> 2이면 float(2), 아니면-> 3~10은 +10

# map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list_data_2 = list(map(lambda x, y: x * y, a, b))
print(list_data_2)

# filter 사용하기
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list_data_3 = list(filter(lambda x: x > 5 and x < 10, a))
print(list_data_3)

# reduce 사용하기
a = [1, 2, 3, 4, 5]
from functools import reduce
list_data_4 = reduce(lambda x, y: x + y, a)
print(list_data_4)
# reduce의 반환값이 15가 나왔습니다. 함수 f에서 x + y를 반환하도록 만들었으므로 
# reduce는 요소 두 개를 계속 더하면서 결과를 누적합니다.