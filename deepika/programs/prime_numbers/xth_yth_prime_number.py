prime_nos = []


def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return
    else:
        prime_nos.append(num)


x = int(input("enter the first value:"))
y = int(input("enter the first value:"))
limit = max(x, y)

i = 2
while len(prime_nos) <= limit:
    check_prime(i)
    i = i + 1
A = prime_nos[x - 1]
B = prime_nos[y - 1]
C = (A * B) - 1
print(C)
