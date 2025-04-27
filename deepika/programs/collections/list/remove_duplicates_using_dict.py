items = int(input("enter number of items:"))
my_list = [input("enter the item:") for i in range(items)]
print(my_list)
keys = dict.fromkeys(my_list)
unique_list = list(keys)
print(unique_list)

# my_list=[]
# for i in range(items):
#     value=input("enter the value:")
#     my_list.append(value)
# print(my_list)
