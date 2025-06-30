#
# Week 12: Data Analysis Final
#
# Author: Estefania Ortiz
#
import sys
data_set = []
with open("life-expectancy.csv") as data_file:
    for line in data_file:
        #print(line.split(,))
        if line.startswith("Entity"): continue;

        row = line.split(",")
        row[2] = int(row[2])
        row[3] = float(row[3])
        data_set.append(row)

#min - max
min_exp = 1000
min_year = None
min_country = None

for i in data_set:
    if i[3] < min_exp:
        min_exp = i[3]
        min_year = i[2]
        min_country = i[0]

max_exp = 0
max_year = None
max_country = None

for i in data_set:
    if i[3] > max_exp:
        max_exp = i[3]
        max_year = i[2]
        max_country = i[0]

print(f"The overall max life expectancy is: {max_exp} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_exp} from {min_country} in {min_year}")

input_year = int(input("Enter the year of interest (1950 - 2019): "))

if input_year not in range (1950, 2019):
    print("Sorry, the year is not in range.")
    sys.exit(0)

year_list = []

for i in data_set:
    if i[2] == input_year:
        year_list.append(i)

min_exp = 1000
min_year = None
min_country = None

for i in year_list:
    if i[3] < min_exp:
        min_exp = i[3]
        min_year = i[2]
        min_country = i[0]

max_exp = 0
max_year = None
max_country = None
sum = 0

for i in year_list:
    sum += i[3]
    if i[3] > max_exp:        
        max_exp = i[3]
        max_year = i[2]
        max_country = i[0]

avg = sum / len(year_list)

print(f"For the year {input_year}:")
print(f"The average life expectancy across all countries was {avg:.2f}")
print(f"The max life expectancy was in {max_country} with {max_exp} in {max_year}")
print(f"The min life expectancy was in {min_country} with {min_exp} in {min_year}")