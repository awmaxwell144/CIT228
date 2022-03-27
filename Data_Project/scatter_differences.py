import csv
from matplotlib import pyplot as plt

filename = 'time-spent-with-relationships-by-age-us.csv' # looks for file in cwd
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    ages, alone, children = [], [], []
    for row in reader:
        try:
            ages.append(int(row[2]))
            alone.append(float(row[3])) 
            children.append(float(row[5]))
        except ValueError:
            print(row[2] + ' missing data')

    plt.subplots(dpi=128, figsize=(10, 6))
    plt.scatter(alone, children, c = ages, cmap = plt.cm.gist_rainbow)
    plt.title("Time Spent With Children Versus Time Spent Alone By Age", fontfamily = 'Times New Roman', fontsize = 22, y = 1.05)
    plt.ylabel('Time Spent With Children (Minutes)', fontfamily = 'Times New Roman', fontsize = 14)
    plt.xlabel('Time Spent Alone (Minutes)', fontfamily = 'Times New Roman', fontsize = 14)
    plt.plot([150,300],[150,300], c = 'grey', ls = '--', label = 'Time Spent Alone Equal To\nTime Spend With Children')
    cbar = plt.colorbar()
    cbar.set_label('Age', rotation=270, fontfamily = 'Times New Roman', labelpad = 20, fontsize = 12)
    plt.xlim(150,500)
    plt.ylim(0,300)
    plt.legend(loc = 'upper right', fontsize = 8)
    plt.rcParams.update({'font.family':'Times New Roman'})
    plt.show()
