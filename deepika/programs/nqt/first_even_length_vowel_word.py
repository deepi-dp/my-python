# starting of the element should be a vowel
# length of a element should be even

sentence = (input("Enter the word:"))
words = sentence.split()
for i in words:
    first_char = i[0]
    if (first_char == "a" or first_char == "e" or first_char == "i" or first_char == "o" or first_char == "u") and len(i) % 2 == 0:
        print(i)
        break
else:
    print("00")
