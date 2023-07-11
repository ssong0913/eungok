# list

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 빈 리스트 a = list()

# list 더하기
a = [1, 2, 3]
b = [4, 5, 6]
a + b
[1, 2, 3, 4, 5, 6]
# 문자열에서 "abc" + "def" = "abcdef"가 되는 것과 같은 이치

# list 반복하기
a = [1, 2, 3]
a * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
# 문자열에서 "abc" * 3 = "abcabcabc" 가 되는 것과 같은 이치

# list 수정
a = [1, 2, 3]
a[2] = 4 #인덱싱 후 대입
a
[1, 2, 4]

# del 함수를 이용한 list 요소 삭제
a = [1, 2, 3]
del a[1] #인덱싱 후 삭제
a
[1, 3]

# del 슬라이싱 list 요소 삭제
a = [1, 2, 3, 4, 5]
del a[2:] #인덱싱 범위 슬라이싱
a
[1, 2]

#리스트 요소 제거 - remove
a = [1, 2, 3, 1, 2, 3]
a.remove(3) #인덱스가 아니고 요소
a
[1, 2, 1, 2, 3] #첫번쨰 3만 삭제 (첫번째부터 순서대로 삭제)

a.remove(3) #한번 더 3 삭제
a
[1, 2, 1, 2]

#리스트 요소 끄집어 내서 삭제 - pop
c = [1, 2, "ㅁ"]
c.pop() #뒤에서부터 삭제, 인덱싱 후 삭제
"ㅁ"
a
[1, 2]

# 리스트에 요소 추가하기 - append
# append(x)는 리스트의 맨 마지막에 x를 추가하는 함수
a = [1, 2, 3]
a.append(4) # append()로 추가. 
a
[1, 2, 3, 4]

# 리스트에 요소 삽입 - insert
# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수

a = [1, 2, 3]
a.insert(0, 4)
a
[4, 1, 2, 3]

# extend()
nums = [ 1, 2, 3 ]
nums.extend(['a', 'b'])
nums 
[1, 2, 3, 'a', 'b']
nums.extend([4])

# 리스트 정렬 - sort
# sort 함수는 리스트의 요소를 순서대로 정렬해 준다.
# sort(*, key=None, reverse=False)
# sorted(iterable, /, *, key=None, reverse=False)
a = ["b", "a"]
b = [5, 1, 4, 3, 2]
c= sorted(["b", "a", "c"]) # reverse= 큰거부터 정렬하여 역순
a.sort()
b.sort()
print(a)
print(b)
print(c)

a.sort(reverse=True)
d = sorted(b, reverse=True)
print(a)
b.sort(reverse=True)
print(b)
print(d)

a
[1, 2, 3, 4, 5]
a = ['a', 'c', 'b']
a.sort()
a
['a', 'b', 'c']

# 리스트 뒤집기 - reverse
# reverse 함수는 리스트를 역순으로 뒤집어 준다. 
# 이때 리스트 요소들을 순서대로 정렬한 다음 다시 역순으로 정렬하는 것이 아니라 
#   현재의 리스트를 그대로 거꾸로 뒤집는다.
a = ['a', 'c', 'b', 'd']
f = [1, 3, 2, 'a', 'c', 'b']
g = [1, 2, 'a', 'c', 'b']
h = [1, 'b', 4, 'd', 2, 'a', 7,]
a.reverse()
f.reverse()
g.reverse()
h.reverse()
print(a)
print(f)
print(g)
print(h)
a
['d','b', 'c', 'a']

# key
# 정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
# key 값을 기준으로 정렬되고 기본값은 오름차순이다
str_list = ['좋은하루','good_morning','굿모닝','niceday'] # 길이가 짧은것부터 
print(sorted(str_list, key=len))

# 인덱스 반환 - index
# index(x) 함수는 리스트에 x 값이 있으면 x의 인덱스 값(위칫값)을 리턴한다.
a = [1, 2, 3]
a.index(3)
2
a.index(1)
0
# 다음 예에서 값 0은 a 리스트에 존재하지 않기 때문에 오류가 발생
# a.index(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 0 is not in list

# count 함수
# 변수. count(찾는 요소)
a = [1, 1, 1, 2, 3]
print(a.count(1))

#clear 함수
a = [1, 1, 1, 2, 3]
a.clear()
print(a)

a.append(5)
print(a)

a.extend([3,4])
print(a)

a.append([3,4])
print(a)
