prime_nos = []
limit = int(input("enter the number:"))


def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        prime_nos.append(num)


i = 2  # we know that first prime number is 2
while len(prime_nos) < limit:
    check_prime(i)
    i = i + 1
for j in prime_nos:
    print(j)
