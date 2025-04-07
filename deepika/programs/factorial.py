num=int(input("enter the value:"))
factorial=1
if num==0:
    print("the factorial of 0 is 1")
elif num<0:
    print("no factorial for negative numbers")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)