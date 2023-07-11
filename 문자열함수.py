str = "Hello"
for i in range(0, len(str)):
    print(f'{str[i]}_', end="\n")

str_1 = "Hello World"

str_1
print(str_1.count("l"))
str_1.upper()

# 문자열 대문자로 변경하는 함수 (string.upper)
s1 = "rich"
s2 = s1.upper()
print(s2)

# 문자열 소문자로 변경하는 함수 (string.lower)
s1 = "RICH"
s2 = s1.lower()
print(s2)

# 문자가 대문자인지 확인하는 함수 (string.isupper)
s1 = "Rich"
s2 = s1.isupper()
print(s2)

# 문자가 소문자인지 확인하는 함수 (string.islower)
s1 = "rich"
s2 = s1.islower()
print(s2)

# 단어의 첫문자를 대문자로 바꿔주는 함수(string.title)
s1 = "rich"
s2 = s1.title()
print(s2)

# 대문자를 소문자로, 소문자를 대문자로 바꿔주는 함수(swapcase)
s1 = "RicH"
s2 = s1.swapcase()
print(s2)

# replace 특정 단어를 다른 단어로 치환
a = "Hello World"
b = a.replace("Hello", "Hi")
print(b)

# Split 문자열을 분리해서 리스트로 만들어 준다.
# str.split(sep=None, maxsplit=- 1)
# .split(sep=" ", maxsplit=) ""값을 기준으로 분리, maxsplit 최대 분리 갯수
c = a.split() # 괄호안에 아무것도 없으면 공백을 기준으로 분리
print(c)
c = a.split("l")
print(c)


# splitlines() 한줄씩 분리
str = '''안녕하세요.
반갑습니다.
어서오세요~
'''
result = str.splitlines()
print(result)