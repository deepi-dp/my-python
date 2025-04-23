# Find Common Height Difference or Detect Invalid Input.
# Given the height of a tree for 4 consecutive weeks, calculate the difference between each week.
# If any height is negative, return "Not valid inputs"
# If any two weekly differences are the same, return that difference.
# If all differences are different, return "None"
# Input1: 2,4,6,7 Output1: 2
# Input2: 5,10,11,13 Output2: None
# Input3:-1,3,4,5 Output3: Not valid inputs


num1=int(input("enter the first value:"))
num2=int(input("enter the second value:"))
num3=int(input("enter the third value:"))
num4=int(input("enter the fourth value:"))

diff1=num2-num1
diff2=num3-num2
diff3=num4-num3
if num1<0 or num2<0 or num3<0 or num4<0:
    print("Not valid inputs")
elif diff1==diff2:
    print(diff1)
elif diff2==diff3:
    print(diff2)
elif diff3==diff1:
    print(diff3)
else:
    print("None")


