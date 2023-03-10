import matplotlib
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
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

    print('hello')

    with open('ar3.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))




    r1end=0
    r1start=0
    tr1= []
    tr2 = []
    r2start = 0
    r2end=0
    with open('rep.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)

            lamda1.append(double(row[1]))

            s1 += 5
    print(tr1)
    #
    # t=0
    # lt=[]
    # lv=[]
    # with open('1l.csv', 'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter=',')
    #     for row in plots:
    #         # t.append(math.floor(double(row[0])))
    #         # t.append(str(row[0]))
    #         lt.append(t)
    #         t += 5
    #         lv.append(double(row[1]))

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex=True)  # create the canvas for plotting

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
    with open('rep.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectar.append(sectr)
            sectr += 5
            secr.append(double(row[1]))

    acqt = 0
    acq = []
    acqta = []
    with open('ar.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqta.append(acqt)
            acqt += 5
            acq.append(double(row[1]))

    acqtr = 0
    acqr = []
    acqtar = []
    with open('rep.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqtar.append(acqtr)
            acqtr += 5
            acqr.append(double(row[1]))

    # fig, ax1 = plt.subplots()
    #
    # fig, [[ax1x, ax1y], [ax2x, ax2y], [ax3x, ax3y], [ax4x, ax4y]] = plt.subplots(nrows=4, ncols=2)
    #axt = ax1.twinx()
    # ##ax1.plot(t5, lamda5)

    ax1.plot(secta, sec, label='Event Arrival rate ' )
    ax1.plot(sectar, secr, label='Maximum Consumption rate' )

    #ax1.set_frame_on(False)  # make it transparent
    #ax1.set_xticks([])
    #ax1.set_xticklabels([])

    ax2.plot(acqta, acq, label='sec ??s')
    ax2.plot(acqtar, acqr, label='sec ??s')
    #ax2.set_xticks([])

    ax3.plot(t15, lamda15, label='Issuer ??s Arrival rate')
    ax3.plot(t1, lamda1, label='Maximum consumption rate \n (number of replicas)')
    #ax3.set_xticks([])

    #
    #ax4.plot(lt, lv, 'r', label='latency (ms)')
    # ax4.plot(tr1, lr1, 'black',  label='latency 2nd replica (ms)')
    # ax4.plot(tr2, lr2, 'g' , label='latency 2nd replica (ms)')



    # #
    # #ax1.legend())
    #
    ax1.set_ylabel('Security \n ??s', fontdict=font)
    ax2.set_ylabel('MerchantBank \n ??s', fontdict=font)
    ax3.set_ylabel('ClientBank \n ??s', fontdict=font)
    ax4.set_ylabel('End-to-end  \n latency (ms)', fontdict=font)




    ax4.set_xlabel('Time (sec)', fontdict=font)
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

