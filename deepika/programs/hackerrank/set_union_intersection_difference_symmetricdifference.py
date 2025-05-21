"""The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.
Output Format:
Output the total number of students who have at least one subscription.
Sample Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output
13"""

# union:A|B ,A.union(B)
n = int(input())
A = set(map(int, input().split()))
r = int(input())
B = set(map(int, input().split()))
output = A.union(B)
print(len(output))

# difference:A-B,A.diiference(B)
# output = A.difference(B)

# intersection:A&B,A.intersection(B)
# output = A.intersection(B)

# symmetric_difference:A^B,A.symmetric_difference(B)
# output = A.symmetric_difference(B)