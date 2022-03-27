import csv
from matplotlib import pyplot as plt

def listAvg(list):
    sum = 0
    for item in list:
        sum += item
    avg = sum / len(list)
    return avg

def pie_chart(lower, upper):
    filename = 'time-spent-with-relationships-by-age-us.csv' # looks for file in cwd
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        alone, friends, children, family, partner, coworkers = [], [], [], [], [], []
        labels = 'Alone','Friends','Children','Family','Partner','Coworkers'
        wedgeColors = 'royalblue','darkorange','teal','purple','magenta','brown'

        for row in reader:
            if int(row[2]) in range(lower, upper):
                try:
                    alone.append(float(row[3])) 
                    friends.append(float(row[4]))
                    children.append(float(row[5]))
                    family.append(float(row[6]))
                    partner.append(float(row[7]))
                    coworkers.append(float(row[8]))
                except ValueError:
                    print(row[2] + ' missing data')
    avgs = []
    avgs.append(listAvg(alone))
    avgs.append(listAvg(friends))
    avgs.append(listAvg(children))
    avgs.append(listAvg(family))
    avgs.append(listAvg(partner))
    avgs.append(listAvg(coworkers))

    title = 'Who Americans Between ' + str(lower) + ' and ' +  str(upper) + ' Spend Their Time With'
    fig1, ax1 = plt.subplots(dpi=128, figsize=(10, 6))
    ax1.pie(avgs, labels = labels, autopct='%3.1f%%', startangle = 0, colors = wedgeColors)
    ax1.axis('equal')
    plt.title(title,  fontsize = 20)
    plt.rcParams.update({'font.family':'Times New Roman'})
    plt.show()

pie_chart(70,80)
    

