name = input("Enter your name:")
char_dict = {}
for ch in name:
    if ch in char_dict:
        char_dict[ch] = char_dict[ch] + 1
    else:
        char_dict[ch] = 1

print(char_dict)

# sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
# print(sorted_dict)
# print(sorted_dict[1][0])
