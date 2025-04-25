num=int(input("enter the number:"))
if num<=1:
    print("is not  prime number")
else:
    for i in range(2,num):
        if num%i ==0:
            print("the no is not a prime number")
            break
    else:
        print("prime number")

