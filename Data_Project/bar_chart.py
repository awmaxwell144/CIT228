import csv
from matplotlib import pyplot as plt
import numpy as np 

filename = 'time-spent-with-relationships-by-age-us.csv' # looks for file in cwd
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    ages, alone, friends, children, family, partner, coworkers = [], [], [], [], [], [], []
    labels = 'Alone','Friends','Children','Family','Partner','Coworkers'
    wedgeColors = 'royalblue','darkorange','teal','purple','magenta','brown'
    lower = 60
    upper = 70 
    for row in reader:
        if int(row[2]) in range(lower,upper):
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

barWidth = .1
br1 = np.arange(len(ages)) + lower
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3] 
br5 = [x + barWidth for x in br4]
br6 = [x + barWidth for x in br5] 

title = 'Who Americans Between ' + str(lower) + ' and ' +  str(upper) + ' Spend Their Time With'
fig1, ax1 = plt.subplots(dpi=128, figsize=(10, 6))
plt.bar(br1,alone, color="navy",  width=barWidth, label="Alone")
plt.bar(br2, friends, color ='darkorange', width=barWidth, label="Friends") 
plt.bar(br3,children, color="teal", width=barWidth,  label="Children")
plt.bar(br4,family, color="purple",  width=barWidth, label="Family")
plt.bar(br5, partner, color ='magenta', width=barWidth, label="Partner") 
plt.bar(br6,coworkers, color="brown", width=barWidth,  label="Coworkers")
plt.title(title,  fontsize = 20, fontfamily = 'Times New Roman',)
plt.ylabel('Minutes', fontfamily = 'Times New Roman', fontsize = 16)
plt.xlabel('Age', fontfamily = 'Times New Roman', fontsize = 16)
plt.legend(loc = 'best', fontsize = 6)
plt.rcParams.update({'font.family':'Times New Roman'})
plt.show()

