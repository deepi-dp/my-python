num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
sum=num1+num2
sum=str(sum)
print(type(sum))

if sum==sum[::-1]:
    print("the number is palindrome")
else:
    print("not a palindrome")

