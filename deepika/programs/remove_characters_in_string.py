A = input("Enter the value of A:")
B = input("Enter the value of B:")

output = ""
for i in A:
    if i not in B:
        output = output + i
print(f"Output: {output}")
