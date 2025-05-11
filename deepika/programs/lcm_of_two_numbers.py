num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
max_num = max(num1, num2)
i=max_num
while True:
    if i % num1 == 0 and i % num2 ==0:
        print(i)
        break
    i=i+1

