v = int(input("enter total number of vehicles:"))
w = int(input("enter total number of wheels:"))
y = (w // 2) - v
x = v - y
if w % 2 != 0 or w > 4 * v or w < 2 * v:
    print("Not Valid")
else:
    print(f"TW={x} , FW={y}")
