s1 = set([1, 1, 1, 1, 2, 1, 1, 2, 3])
print(s1) # 중복은 1개만 표시
s2 = set("Hello World")
print(s2)

s3 = list("Hello World")
print(s3)

s4 = tuple("Hello World")
print(s4)
# ↑ s2, s3, s4 공백도 요소로

s5 = set(tuple(list(set("Hello World"))))
print(s5)

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 구하기
#  ‘&’를 이용
s3 = s1 & s2
print(s3)
# intersection 함수를 사용해도 결과는 동일
s4 = s1.intersection(s2)
print(s4)

# 합집합 구하기
# ‘|’를 사용하면 합집합을 구할 수 있다.
# 중복해서 포함된 값은 1개씩만 표현
s5 = s1 | s2
print(s5)
# union 함수를 사용해도 된다.
s6 = s1.union(s2)
print(s6)

# 차집합 구하기
# -(빼기)를 사용하면 차집합을 구할 수 있다.
s7 = s1 - s2
print(s7)
s8 = s2 - s1
print(s8)
# difference 함수를 사용해도 차집합을 구할 수 있다.
s9 = s1.difference(s2)
print(s9)
s10 = s2.difference(s1)
print(s10)

# 값 1개 추가하기 - add
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러 개 추가하기 - update
s1 = set([1, 2, 3])
s1.update([1, 2, 4, 5, 6])
print(s1)

# 특정 값 제거하기 - remove
s1 = set([1, 2, 3, 4, 5, 6, 7])
s1.remove(2)
print(s1)