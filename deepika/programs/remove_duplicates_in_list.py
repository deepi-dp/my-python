colors = ['black', 'red', 'green', 'red', 'blue', 'black']


# unique_colors=list(set(colors))
# print(unique_colors)

def remove_duplicates(colors):
    unique_colors = list(set(colors))
    return unique_colors


unique_colors = remove_duplicates(colors)
print(unique_colors)
