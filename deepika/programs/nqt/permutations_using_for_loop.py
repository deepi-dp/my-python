str = 'ABC'
for i in str:
    for j in str:
        if j != i:
            for k in str:
                if k != i and k != j:
                    word = i + j + k
                    print(word)
