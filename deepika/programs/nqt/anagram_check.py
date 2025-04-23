# Anagram Check
# Given two strings s1 and s2, check if they are anagrams
# • If lengths are not equal or any input is empty, print "Invalid Input".
# . If both strings have the same characters with the same frequency print "true", else print "false"
# Input: abaac aabca
# Output:true

s1 = input("enter the first word:")
s2 = input("enter the second word:")

if len(s1) != len(s2) or s1 == '' or s1 is None or s2 == '' or s2 is None:
    print("Invalid input")
else:
    str1 = ''.join(sorted(s1))
    str2 = ''.join(sorted(s2))
    if str1 == str2:
        print("true")
    else:
        print("false")
