#
with open("life-expectancy.csv") as data_file:

    for line in data_file:
        #print(line.split(","))
        if line.startswith("Entity"): continue;

        row = line.split(",")
        row[2] = int(row[2])
        row[3] = float(row[3])