# Balance '*' and '#'
# Given a string made of '*' and '#",determine how many more of each character you need to add to make
# the string valid (where the number of '*' and '#' are equal)
# Problem:
# • If '*' > '#', output a positive integer showing how many '*' are extra.
# • If '#' > '*', output a negative integer showing how many '#' are extra,
# • If'*'= '#, output 0
# Input: ###*** Output: 0
# Input: #****## Output: 1
# Input: #**### Output: -2

string = input("enter the string:")
star_count = 0
hash_count = 0
for char in string:
    if char == "*":
        star_count = star_count + 1
    elif char == "#":
        hash_count = hash_count + 1
if "*" > "#":
    print(star_count-hash_count)
elif "#" > "*":
    print(hash_count-star_count)
else:
    print(0)
