def add(x, y):
    return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

print("사칙연산을 선택 해!!!")
print("1.Add")
print("2.Diff")
print("3.times")
print("4.div")

choice = input("선택 하세요(1/2/3/4):")

num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

if choice == '1':
  print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
  print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
  print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
  print(num1,"/",num2,"=", divide(num1,num2))
else:
  print("잘못된 선택")