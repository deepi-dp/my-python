# 2 4 6 8 10 12 14 16 18 20
inputs_count = int(input("enter the number of inputs:"))

# num = int(input("enter the number of inputs:"))
list = []
my_list = []
for i in range(0, inputs_count):
    num = int(input("enter the value:"))
    list.append(num)
max_num = max(list)

for i in range(2, max_num + 1, 2):
    my_list.append(i)
print(my_list)

for num in list:
    if num not in my_list:
        print(num)

# if list in my_list:
#     print(f"{(list[inputs_count - 1]) + 2}")

#     # print(i)
# if i not in input2:
#     print()
