# Pratheev numbers: A number whose cube, when split into three parts, sums up to the number itself.
# Example: 8, 134, 4949, 5049, 5455, 5554, 7172
def pratheev_number(number):
    cube = str(number ** 3)
    # print(f'cube:{cube}')
    if len(cube) > 2:
        limit = len(cube) // 3
        left = int(cube[:limit])
        center = int(cube[limit: limit * 2])
        right = int(cube[limit * 2:])
        output = left + center + right
        if output == number:
            print(number, end=', ')
        else:
            pass
    else:
        print("Invalid input")


print("Starting!")
for i in range(1, 10000):
    pratheev_number(i)

print('Completed!')
