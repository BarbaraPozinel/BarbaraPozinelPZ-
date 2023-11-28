hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

people = {"Eva": ["female", "white", "blonde", "blue", "oval"],
        "Larisa": ["female", "white", "brown", "brown", "oval"],
        "Matej": ["male", "white", "black", "blue", "oval"],
        "Miha": ["male", "white", "brown", "green","square"]}

with open(r"C:\Users\Admin\Downloads\dna.txt", "r") as dna_file:
        dna = dna_file.read()

person = []

for x in gender:
        if gender[x] in dna:
                print(x)
                person.append(x)
for x in race:
        if race[x] in dna:
                print(x)
                person.append(x)
for x in hair:
        if hair[x] in dna:
                print(x)
                person.append(x)
for x in eye_color:
        if eye_color[x] in dna:
                print(x)
                person.append(x)
for x in facial_shape:
        if facial_shape[x] in dna:
                print(x)
                person.append(x)

for y in people:
        if people[y] == person:
                print("The person we are looking for is: {}".format(y))
                break