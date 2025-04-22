temp1 = int(input("enter the first temperature value:"))
temp2 = int(input("enter the second temperature value:"))
if temp1 < 10:
    print("it's very cool")
else:
    if temp1 == range(10, 21):
        print("it's cold")
    elif temp1 > 20:
        print("it's warm")
if temp2 < 10:
    print("it's very cool")
else:
    if temp2 == range(10, 21):

        print("it's cold")
    elif temp2 > 20:
        print("it's warm")

print(f"the average of temp1 and temp2 is", {(temp1 + temp2) / 2})
print(temp2, temp1)
