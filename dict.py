# dictionary(딕셔너리)
# 딕셔너리 타입은 키(key)와 값(value)으로 되어 있는 순서가 없는 집합
# 중괄호로 되어 있고 키와 값이 있습니다.
{"a" : 1, "b":2}
{'a': 1, 'b': 2}
# 키로는 immutable(변경 불가)한 값은 사용할 수 있지만, 
#          mutable(변경 가능)한 객체는 사용할 수 없습니다.

# immutable 예
a = {1: 5, 2: 3}   # int 사용
a
{1: 5, 2: 3}
a2 = {(1,5): 5, (3,3): 3} # tuple사용
a
{(1, 5): 5, (3, 3): 3}
a3 = { 3.6: 5, "abc": 3} # float 사용
a
{3.6: 5, 'abc': 3}
a4 = { True: 5, "abc": 3} # bool 사용
a
{True: 5, 'abc': 3}

# mutable 예
""" a = { {1, 3}: 5, {3,5}: 3}     #set 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
a = {[1,3]: 5, [3,5]: 3}     #list 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
a = { {"a":1}: 5, "abc": 3}     #dict 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict' """

# 값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워집니다.
{"a" : 1, "a":2}
{'a': 2}
print({"a" : 1, "a":2})

# 순서가 없기 때문에 인덱스로는 접근할수 없고, 키로 접근 할 수 있습니다.
d = {'abc' : 1, 'def' : 2}
""" d[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0 """
d['abc']
1
print(a2[(1,5)])

# keys(), values(), items()
print(a.keys())
print(a.values())
print(a.items())

# dict 만들기
result = dict([('a',1), ('b',2), ('c',3)])
print(result)

# 키로 접근하여 값을 변경할 수 있습니다.
d['abc'] = 5
d
{'abc': 5, 'def': 2}

# 새로운 키와 값을 아래와 같이 추가할 수 있습니다.
d['ghi'] = 999
d
{'abc': 5, 'def': 2, 'ghi': 999}

# dictionary(딕셔너리) 선언
# 딕셔너리 선언할때는 빈 중괄호를 사용합니다.
#  (set 중괄호를 이용하지만 빈중괄호로 선언하면 type이 dict가 됩니다.)
e = {}
type(e)
# <class 'dict'>
f = dict()
type(f)
# <class 'dict'>
# dict constructor를 통해서 아래와 같이 바로 키와 값을 할당하며 선언할 수 있습니다.
newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
newdict
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}
print(newdict)

# dictionary(딕셔너리) 변환
# 리스트 속에 리스트나 튜플, 튜플속에 
# 리스트나 튜플의 값을 키와 value를 나란히 입력하면, 
# 아래와 같이 dict로 변형할 수 있습니다.
name_and_ages = [['alice', 5], ['Bob', 13]]
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = [('alice', 5), ('Bob', 13)]
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = (('alice', 5), ('Bob', 13))
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = (['alice', 5], ['Bob', 13])
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}

# 여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
a.update({'bob':99, 'tony':99, 'kim': 30})
a
{'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}
# 있는건 수정하고 없는건 추가한다.
print(a)

# dictionary(딕셔너리) for문

# for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
# 순서는 임의적이다.같은 순서를 보장할 수 없다.
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for key in a:
    print(key)
""" alice
bob
tony
suzy """
# value값으로 for문을 반복하기 위해서는 values() 를 사용해야합니다.
for val in a.values():
    print(val)
""" [1, 2, 3]
20
15
30 """    
# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용합니다.
for key, val in a.items():
    print(key, val)
    print("key = {key}, value={value}".format(key=key,value=val))

""" key = alice, value=[1, 2, 3]
key = bob, value=20
key = tony, value=15
key = suzy, value=30 """

# key값 따로 value 따로 list
key_list = []
value_list = []
for key, value in a.items():
    key_list.append(key)
    value_list.append(value)

print(key_list)
print(value_list)
    