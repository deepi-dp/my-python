# Group Words by Anagrams.
# Given a list of words, write a Python function to group them into sets of anagrams.
# Inputs:['cat', 'dog', 'god', 'tac','act', 'odg']
# Output: [{'cat', 'tac', 'act'},{'dog',god', 'odg'}]

words = input("enter the items separated by comma:")
# cat,dog,tac,act,god,odg
my_list = words.split(",")
# print(my_list)
# {
#     'act': {'cat', 'tac', 'act'},
#     'dgo': {'dog', 'god', 'odg'}
# }
dict = {}
for word in my_list:
    key = "".join(sorted(word))
    if key not in dict:
        dict[key] = {word}
    else:
        dict[key].add(word)
print(dict)
print(list(dict.values()))
