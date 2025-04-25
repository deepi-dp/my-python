num = str(input("enter the value:"))
digits = len(num)
sum = 0
for i in num:
    value = int(i) ** digits
    sum = sum + value
temp = int(num)
if sum == temp:
    print("the given number is armstrong")
else:
    print("not armstrong")
