# Kaprekar numbers: A number whose square, when split into two parts, sums up to the number itself.
# Example: 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4950, 5050, 7272, 7777, 9999
number = int(input("enter the number:"))
square = str(number * number)
# print(f'square:{square}')
if len(square) > 1:
    limit = len(square) // 2
    left = int(square[0:limit])
    right = int(square[limit:])
    output = left + right
    if output == number:
        print('yes')
    else:
        print('no')
else:
    print("Invalid input")

