"""The first line contains integer n , the number of elements in the set s.
The second line contains n space separated elements of set s . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N , the number of commands.
The next  N lines contains either pop, remove and/or discard commands followed by their associated value.
Output Format

Print the sum of the elements of set s on a single line.
Sample Input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
Sample Output
4"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(0, N):
    output = input().split()
    if output[0] == "pop":
        s.pop()
    elif output[0] == "remove":
        s.remove(int(output[1]))
    elif output[0] == "discard":
        s.discard(int(output[1]))
count = 0
for i in s:
    count = count + i
print(count)
