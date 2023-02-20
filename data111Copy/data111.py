


# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import math

import csv

from numpy import double


def graf():
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


    with open('arriss111.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))


    #lr1= [1300, 769, 593, 487, 216, 206, 190, 189,176, 164, 155, 131, 113, 103, 92, 99, 96, 86, 81, 168, 198, 260]
    lr1= [1773, 1573,1080, 830, 849,79.5,67.5,57.3,42.8,197,346,489,634,613,610,591,591,584,565,585,584,579,587,591,618,668,707,743,760,759,758,748,731,722,710,698,690,674,660,643,631,619,607,598,587,576,566,556,546,540,532,524,518,510,503,500,492,487,480,473,467,459,453,444,433,422,662,649,889,1128,855,2341,2072,1803,1794,277,265,252,239,228,215,204,194,184,176,169,160,153,149,143,140]
    #lr2= [863,843, 841, 833, 818, 806, 793, 783, 771, 764, 745, 724, 695, 663, 627, 579, 563, 524, 483, 440, 358, 320, 282]
    lr2 = [3124,3008,2870,2444,2424,2396,2386,608,595,588,576,573,560,547,537,513,496,463,404,384,339,293]

    r1end=0
    r1start=0
    tr1= []
    tr2 = []
    r2start = 0
    r2end=0
    print(len(lr1))
    with open('riss111.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)

            lamda1.append(double(row[1]))
            if str(row[0]) == '2023-01-16 13:41:40' :
                r1start = 1
            if r1start==1 and r1end !=1:
                tr1.append(s1)
            if str(row[0]) == '2023-01-16 13:49:10':
                r1end=1

            if str(row[0]) == '2023-01-16 13:47:20':
                r2start = 1
            if r2start == 1 and r2end != 1:
                tr2.append(s1)
            if str(row[0]) == '2023-01-16 13:49:05':
                r2end = 1
            # if r1start == 1 and double(row[1]) == 525 :
            #     r1end=1
            # if r1end == 1 and double(row[1]) == 350 and r2end != 1 :
            #     r2start = 1
            #     tr2.append(s1)
            # if r2start == 1 and double(row[1]) == 175:
            #     r2end = 1

            s1 += 5
    print(tr1)

    t=0
    lt=[]
    lv=[]
    with open('latency111.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            lt.append(t)
            t += 5
            lv.append(double(row[1]))

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex=True)  # create the canvas for plotting

    # ax4 = plt.subplot(4, 1, 4)
    # ax1 = plt.subplot(4, 1, 1, sharex=ax4)
    # # (2,1,1) indicates total number of rows, columns, and figure number respectively
    # ax2 = plt.subplot(4, 1, 2, sharex=ax4)
    # ax3 = plt.subplot(4, 1, 3, sharex=ax4)

    sect = 0
    sec = []
    secta = []
    with open('ar111.csv', 'r') as csvfile:
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
    with open('r111.csv', 'r') as csvfile:
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
    with open('aracq111.csv', 'r') as csvfile:
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
    with open('racq111.csv', 'r') as csvfile:
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

    ax2.plot(acqta, acq, label='sec µs')
    ax2.plot(acqtar, acqr, label='sec µs')
    #ax2.set_xticks([])

    ax3.plot(t15, lamda15, label='Issuer µs Arrival rate')
    ax3.plot(t1, lamda1, label='Maximum consumption rate \n (number of replicas)')
    #ax3.set_xticks([])

    #
    ax4.plot(lt, lv, 'r', label='latency (ms)')
    ax4.plot(tr1, lr1, label='latency 2nd replica (ms)')
    ax4.plot(tr2, lr2, 'g' , label='latency 2nd replica (ms)')




    # #
    # #ax1.legend())
    #
    ax1.set_ylabel('Security µs')
    ax2.set_ylabel('AcquirerBank')
    ax3.set_ylabel('IssuerBank')
    ax4.set_ylabel('End-to-end  \n latency')




    ax4.set_xlabel('Time (sec)')
    # ax3.set_ylabel('Event Arrival Rate')
    # #
    # ax2.set_ylabel('End to end Latency (ms)')
    # # #
    # # plt.title('Graph Bin pack autoscaler')
    # ax3.legend()
    # # ax1.legend(bbox_to_anchor=(0.21, 0.7))
    # ax4.legend()
    # # #
    ax1.legend(fontsize='x-small')
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    graf()

