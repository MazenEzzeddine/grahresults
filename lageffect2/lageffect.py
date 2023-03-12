


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
    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0


    #############iiiiiiitttttttttttttttttttiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiooooooooooooooooooooooooooooooooooooooooooooooooooyyyyyyyyyyyyyyyyyyyyyyyyyykkkkkkkkkkkkkkkkkiiii


    with open('ar.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))


    lr1= [1300, 769, 593, 487, 216, 206, 190, 189,176, 164, 155, 131, 113, 103, 92, 99, 96, 86, 81, 168, 198, 260]
    lr2= [863,843, 841, 833, 818, 806, 793, 783, 771, 764, 745, 724, 695, 663, 627, 579, 563, 524, 483, 440, 358, 320, 282]

    r1end=0
    r1start=0
    tr1= []
    tr2 = []
    r2start = 0
    r2end=0
    with open('replicas.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)

            lamda1.append(double(row[1]))
            if double(row[1]) == 350 and r1end!=1:
                tr1.append(s1)
                r1start=1
            if r1start == 1 and double(row[1]) == 175 :
                r1end=1
            if r1end == 1 and double(row[1]) == 350 and r2end != 1 :
                r2start = 1
                tr2.append(s1)
            if r2start == 1 and double(row[1]) == 175:
                r2end = 1

            s1 += 5
    print(tr1)

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

#############################################
    t5lag = []
    t15lag = []
    lamda15lag = []
    lamda5lag = []

    t1lag = []
    lamda1lag = []

    s15lag = 0
    s5lag = 0
    s1lag = 0

    #############iiiiiiitttttttttttttttttttiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiooooooooooooooooooooooooooooooooooooooooooooooooooyyyyyyyyyyyyyyyyyyyyyyyyyykkkkkkkkkkkkkkkkkiiii

    with open('ar.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15lag.append(s15)
            s15lag += 5
            lamda15lag.append(double(row[1]))

    lr1 = [1300, 769, 593, 487, 216, 206, 190, 189, 176, 164, 155, 131, 113, 103, 92, 99, 96, 86, 81, 168, 198, 260]
    lr2 = [863, 843, 841, 833, 818, 806, 793, 783, 771, 764, 745, 724, 695, 663, 627, 579, 563, 524, 483, 440, 358, 320,
           282]

    r1endlag = 0
    r1startlag = 0
    tr1lag = []
    tr2lag = []
    r2startlag = 0
    r2endlag = 0
    with open('replicas.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1lag.append(s1lag)

            lamda1.append(double(row[1]))
            if double(row[1]) == 350 and r1endlag != 1:
                tr1lag.append(s1lag)
                r1startlag = 1
            if r1startlag == 1 and double(row[1]) == 175:
                r1endlag = 1
            if r1endlag == 1 and double(row[1]) == 350 and r2endlag != 1:
                r2startlag = 1
                tr2lag.append(s1lag)
            if r2startlag == 1 and double(row[1]) == 175:
                r2endlag = 1

            s1lag += 5
    print(tr1lag)

    tlag = 0
    ltlag = []
    lvlag = []
    with open('l1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            ltlag.append(tlag)
            tlag += 5
            lag.append(double(row[1]))


##################################

    fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)  # create the canvas for plotting

    # ax4 = plt.subplot(4, 1, 4)
    # ax1 = plt.subplot(4, 1, 1, sharex=ax4)
    # # (2,1,1) indicates total number of rows, columns, and figure number respectively
    # ax2 = plt.subplot(4, 1, 2, sharex=ax4)
    # ax3 = plt.subplot(4, 1, 3, sharex=ax4)

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



    # fig, ax1 = plt.subplots()
    #
    # fig, [[ax1x, ax1y], [ax2x, ax2y], [ax3x, ax3y], [ax4x, ax4y]] = plt.subplots(nrows=4, ncols=2)
    #axt = ax1.twinx()
    # ##ax1.plot(t5, lamda5)

    ax1.plot(secta, sec, label='Event Arrival rate ' )
    ax1.plot(sectar, secr, label='Maximum Consumption rate' )
    ax2.plot(lt, lv, 'r', label='latency (ms)')
   #ax4.plot(tr1, lr1, label='latency 2nd replica (ms)')

    #ax1.set_frame_on(False)  # make it transparent
    #ax1.set_xticks([])
    #ax1.set_xticklabels([])







    # #
    # #ax1.legend())
    #
    ax1.set_ylabel('Security µs', fontdict=font)
    ax2.set_ylabel('End to end latency (ms)', fontdict=font)




    ax1.set_xlabel('Time (sec)', fontdict=font)
    # ax3.set_ylabel('Event Arrival Rate')
    # #
    # ax2.set_ylabel('End to end Latency (ms)')
    # # #
    # # plt.title('Graph Bin pack autoscaler')
    # ax3.legend()
    # # ax1.legend(bbox_to_anchor=(0.21, 0.7))
    # ax4.legend()
    # # #
    ax1.legend(fontsize='small')
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    graf()

