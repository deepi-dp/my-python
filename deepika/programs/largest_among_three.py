num1=int(input("enter the first value:"))
num2=int(input("enter the second value:"))
num3=int(input("enter the third value:"))
if num1>num2 and num1>num3:
    greatest_num = num1
elif num2>num1 and num2>num3:
    greatest_num = num2
else:
    greatest_num = num3

print(f"Greatest number is {greatest_num}")
