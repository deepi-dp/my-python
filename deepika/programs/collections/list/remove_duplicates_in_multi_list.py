multi_colors = [
    ['black', 'red', 'green', 'red', 'blue', 'black'],
    ['red', 'green', 'black'],
    ['orange', 'yellow', 'green', 'red', 'blue', 'yellow'],
    ['black', 'black', 'black']
]


def remove_duplicates(colors):
    unique_colors = list(set(colors))
    return unique_colors


for item in multi_colors:
    unique_colors = remove_duplicates(item)
    print(unique_colors)
