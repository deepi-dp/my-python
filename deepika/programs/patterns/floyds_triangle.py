num=int(input("enter the number of rows:"))
count=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(count,end=' ')
        count=count+1
    print()

# 1
# 2 3
# 4 5 6
