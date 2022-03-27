import csv
from matplotlib import pyplot as plt

filename = 'time-spent-with-relationships-by-age-us.csv' # looks for file in cwd
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    ages, alone, friends, children, family, partner, coworkers = [], [], [], [], [], [], []
    for row in reader:
        try:
            ages.append(int(row[2]))
            alone.append(float(row[3])) 
            friends.append(float(row[4]))
            children.append(float(row[5]))
            family.append(float(row[6]))
            partner.append(float(row[7]))
            coworkers.append(float(row[8]))
        except ValueError:
            print(row[2] + ' missing data')

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(ages, alone, marker = '.', lw = 1.0, c = 'navy', label = "Alone")
plt.plot(ages, friends, marker = '.', lw = 1.0, c = 'darkorange', label = "Friends")
plt.plot(ages, children, marker = '.', lw = 1.0, c = 'teal', label = "Children")
plt.plot(ages, family, marker = '.', lw = 1.0, c = 'purple', label = "Family")
plt.plot(ages, partner, marker = '.', lw = 1.0, c = 'magenta', label = "Partner")
plt.plot(ages, coworkers, marker = '.', lw = 1.0, c = 'brown', label = "Coworkers")
plt.title('Who Americans Spend Their Time With (By Age)', fontfamily = 'Times New Roman', fontsize = 25)
plt.ylabel('Minutes', fontfamily = 'Times New Roman', fontsize = 16)
plt.xlabel('Age', fontfamily = 'Times New Roman', fontsize = 16)
plt.grid(which='major', axis='y', ls = '--', c = 'grey', lw = 1.0)
plt.xlim(15,80)
plt.ylim(0,500)
plt.legend(loc = 'upper left', fontsize = 8 )
plt.show()
