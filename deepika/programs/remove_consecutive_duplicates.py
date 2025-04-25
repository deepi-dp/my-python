digits = str(input("enter the number:"))
list = []
list.append(digits[0])
for i in range(0, len(digits) - 1):
    a = digits[i]
    b = digits[i + 1]
    if a != b:
        list.append(b)
# print(list)
print("".join(list))

# num = "".join(list)
# print(type(num))
