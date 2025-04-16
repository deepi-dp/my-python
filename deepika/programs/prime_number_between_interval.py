start = int(input("enter the starting number:"))
end = int(input("enter the ending number:"))


def prime_number_or_not(num):
    if num <= 1:
        print(f"{num} is not a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")


for i in range(start,end+1):
    prime_number_or_not(i)
