


# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import matplotlib
import math

import csv

from numpy import double


def graf():
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}

    matplotlib.rc('font', **font)




    t=0
    lt=[]
    lv=[]
    with open('l1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            lt.append(t)
            t += 5
            lv.append(double(row[1]))







    sect = 0
    sec = []
    secta = []
    with open('ar.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            secta.append(sect)
            sect += 5
            sec.append(double(row[1]))

    sectr = 0
    secr = []
    sectar = []
    with open('replicas.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectar.append(sectr)
            sectr += 5
            secr.append(double(row[1]))


##########################################################

    tlag = 0
    ltlag = []
    lvlag = []
    with open('latency2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            ltlag.append(tlag)
            tlag += 5
            lvlag.append(double(row[1]))

    sectlag = 0
    seclag = []
    sectalag = []
    with open('ar2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectalag.append(sectlag)
            sectlag += 5
            seclag.append(double(row[1]))

    sectrlag = 0
    secrlag = []
    sectarlag = []
    with open('replica2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectarlag.append(sectrlag)
            sectrlag += 5
            secrlag.append(double(row[1]))

    fig, ax = plt.subplots(2, 2,
                           sharex='col',
                           sharey='row')

############################################################################
    ax[0,0].plot(secta, sec, label='Event Arrival rate ' )
    ax[0, 0].plot(sectar, secr, label='Maximum Consumption rate' )
    ax[1, 0].plot(lt, lv, 'r', label='latency (ms)')

    ax[0,0].set_ylabel('Security µs', fontdict=font)


    ax[1,0].set_ylabel('End to end latency (ms)', fontdict=font)

    ax[1,0].set_xlabel('Time (sec)', fontdict=font)


    ####################################################
    ax[0,1].plot(sectalag, seclag, label='Event Arrival rate ' )
    ax[0, 1].plot(sectarlag, secrlag, label='Maximum Consumption rate' )
    ax[1, 1].plot(ltlag, lvlag, 'r', label='latency (ms)')

    #####################################################
    # ax3.set_ylabel('Event Arrival Rate')
    # #
    # ax2.set_ylabel('End to end Latency (ms)')
    # # #
    # # plt.title('Graph Bin pack autoscaler')
    # ax3.legend()
    # # ax1.legend(bbox_to_anchor=(0.21, 0.7))
    # ax4.legend()
    # # #
    ax[0,0].legend(fontsize='small')
    ax[0, 0].set(title= "lag not taken into account" )
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    graf()

