import itertools

str = "ABC"
for i in itertools.permutations(str):
    print("".join(i))
