def my_function(x):
    print(x)
    x = x - 1
    if x == 0:
        return x
    else:
        my_function(x)


my_function(5)
print('recursion completed')
