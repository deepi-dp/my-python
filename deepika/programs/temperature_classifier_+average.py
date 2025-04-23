# Given two temperatures, classify each based on the following:
# < 10 "it's very cool"
# 10 to 20 -> "it's cold"
# > 20 -> "it's warm"
# Then:
# Print the category for each temperature
# Print their average (as a double)
# Print both temperatures in reverse order
# input1: 5 25
# Output : it's very cool,it's warm,15.0,25,5


temp1 = int(input("enter the first temperature value:"))
temp2 = int(input("enter the second temperature value:"))


def temp_classifier(temp):
    if temp < 10:
        print("it's very cool", end=",")
    elif 10 <= temp >= 20:
        print("it's cold", end=",")
    else:
        print("it's warm", end=",")


temp_classifier(temp1)
temp_classifier(temp2)

print((temp1 + temp2) / 2, end=",")
print(f"{temp2},{temp1}")
