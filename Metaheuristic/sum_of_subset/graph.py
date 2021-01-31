import csv
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection


def generate_graph():
    '''
    Method which is used to draw graph via matplot library
    :return:
    '''
    file = open('A:\\_MACIEK\\WORK\\Develop\\Metaheuristic\\sum_of_subset\\data\\output\\stats_to_graph.csv', 'rt')
    data = csv.reader(file, delimiter=' ')
    time_brut = []
    time_climb = []
    time_simu = []
    time_tabu = []
    size_brut = []
    size_climb = []
    size_simu = []
    size_tabu = []

    for line in data:
        if str(line[0])=='Brut':
            size_brut.append(int(line[1]))
            time_brut.append(float(line[4]))
        elif str(line[0])=='Clim':
            size_climb.append(int(line[1]))
            time_climb.append(float(line[4]))
        elif str(line[0])=='Simu':
            size_simu.append(int(line[1]))
            time_simu.append(float(line[4]))
        elif str(line[0])=='Tabu':
            size_tabu.append(int(line[1]))
            time_tabu.append(float(line[4]))

    xdata1 = size_brut[:]
    ydata1 = time_brut[:]
    xdata2 = size_climb[:]
    ydata2 = time_climb[:]
    xdata3 = size_simu[:]
    ydata3 = time_simu[:]
    xdata4 = size_tabu[:]
    ydata4 = time_tabu[:]
    xdata1.sort()
    ydata1.sort()
    xdata2.sort()
    ydata2.sort()
    xdata3.sort()
    ydata3.sort()
    xdata4.sort()
    ydata4.sort()


    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(xdata1, ydata1, color='tab:blue', label='Bruteforce')
    ax.plot(xdata2, ydata2, color='tab:green', label='Climbing')
    ax.plot(xdata3, ydata3, color='tab:orange', label='Simulated-Annealing')
    ax.plot(xdata4, ydata4, color='tab:red', label='Tabu')



    xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05, orientation='vertical')
    xevents2 = EventCollection(xdata2, color='tab:green', linelength=0.05, orientation='vertical')
    xevents3 = EventCollection(xdata3, color='tab:orange', linelength=0.05, orientation='vertical')
    xevents4 = EventCollection(xdata4, color='tab:red', linelength=0.05, orientation='vertical')



    yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05, orientation='vertical')
    yevents2 = EventCollection(ydata2, color='tab:green', linelength=0.05, orientation='vertical')
    yevents3 = EventCollection(ydata3, color='tab:orange', linelength=0.05, orientation='vertical')
    yevents4 = EventCollection(ydata4, color='tab:red', linelength=0.05, orientation='vertical')



    ax.add_collection(xevents1)
    ax.add_collection(xevents2)
    ax.add_collection(xevents3)
    ax.add_collection(xevents4)
    ax.add_collection(yevents1)
    ax.add_collection(yevents2)
    ax.add_collection(yevents3)
    ax.add_collection(yevents4)



    ax.set_xlim([10, 20])
    ax.set_ylim([0, 1])
    ax.legend()
    ax.set_title('Graph of estimated time of generated solution')
    plt.show()


generate_graph()