with open("../Lekcija3/people.csv","r") as people_file:
    vsebina = people_file.read().splitlines()

    for row in vsebina:
        row_data = row.split(",")
    print("{0} is {1} Years old and is a {2}.".format(row_data[0], row_data[1], row_data[2]))