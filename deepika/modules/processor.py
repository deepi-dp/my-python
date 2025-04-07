from person_module import persons

person1 = persons['person1']
person2 = persons['person2']

details = lambda a: print(f"{a['name']} is from {a['country']} and his age is {a['age']}")

details(person1)
details(person2)
