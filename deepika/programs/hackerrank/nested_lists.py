# There are  students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry,
# so we order their names alphabetically and print each name on a new line.
# output:
# Berry
# Harry

records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
names = []
scores = []
for item in records:
    scores.append(item[1])
sorted_scores = list(set(scores))
sorted_scores.sort()
sec_lowest_score = sorted_scores[1]

for item in records:
    if item[1] == sec_lowest_score:
        names.append(item[0])
names.sort()
for name in names:
    print(name)
