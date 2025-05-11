str = input("enter the word:")
num = int(input("enter the ascii value:"))
print(f"Character of Ascii value {num} is {chr(num)}")
for char in str:
    print(f"{char} - {ord(char)}")
