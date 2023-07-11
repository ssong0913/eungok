t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# print(type(t4))

print(t5[0])
print(t5[2][1])

# indexing

t1 = (1, 2, 'a', 'b')
print(t1[0])

# slicing
t1 = (1, 2, 'a', 'b', 'c')
print(t1[1:])
print(t1[-2:])
print(t1[:-2])
print(t1[-3:4])

# 원소의 갯수
t1 = (1, 2, 'a', 'b', 'c')
print(len(t1))

# for i in range(len(t1)):
#     print("안녕하세요")

for i in range(len(t1)):
    print("안녕하세요")
    print(t1[i])

# tuple 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
t3 = (1, 2, 'a', 'b', 3, 4)

print(t1+t2)

# tuple 곱하기
t2 = (3, 4)
t4 = t2 * 3
t4 = (3, 4, 3, 4, 3, 4)

print(t4)
print((t1+t2)*3)

print(tuple([1,2,3]))

print(range(10))