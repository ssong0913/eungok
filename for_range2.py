# for num in range(0, 101, 2):
#     sum += num
#     print("짝수의 합",num)

total_sum = 0
for num in range(1,101):
    if num % 2 == 1:
        continue
    total_sum += num
print("홀수의 합:", total_sum)

total_sum = 0
for num in range(1,101):
    if num % 2 == 0:
        continue
    total_sum += num
print("짝수의 합:", total_sum)
