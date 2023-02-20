
import matplotlib.pyplot as plt
import math

import csv

from numpy import double

# https://snapshots.raintank.io/dashboard/snapshot/tvr11TUPeg514X0g1V1M70z2biS9x9PL?orgId=2
def graf():
    sect = 0
    sec = []
    secta = []
    with open('arn177.csv', 'r') as csvfile:
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
    with open('rn177.csv', 'r') as csvfile:
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
    with open('acqn1777.csv', 'r') as csvfile:
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
    with open('acqr177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqtar.append(acqtr)
            acqtr += 5
            acqr.append(double(row[1]))



    #########################################################
    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0



    with open('arissuer177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))

    t = 0
    tp =0
    lt = []
    lv = []
    r1start=0
    r1end=0
    tr1 = []
    lr1c = 0
    r1start = 1

    tr2 = []
    lr2 = []
    lr2c=0

    tr3 = []

    #####################################################
    r2start = 0
    r2end=0

    r3start = 0
    r3end=0

    with open('riss177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)
            lamda1.append(double(row[1]))
            s1 += 5
            if r1start and r1end == 0:
                    # lr1.append(str(row[1]))
                    tr1.append(s1)
                    lr1c += 1
            if lr1c == 35:
                r1end = 1
            if str(row[0])=="2023-01-19 17:17:30":
                r2start = 1
            if r2start and r2end==0 :
                        tr2.append(s1)
            if str(row[0])=="2023-01-19 17:39:45":
                r2end=1
            if str(row[0]) == "2023-01-19 17:53:30":
                r3start = 1
            if r3start and r3end == 0:
                tr3.append(s1)
            if str(row[0]) == "2023-01-19 18:17:00":
                r3end = 1

        print(tr3)




    # lr1= [887,1373,1528,2100,2076,1809,1542,775,754,737,718,694,684,667,644,624,599,572,555,542,510,455,419,381,362,369,356,345,335,324,
    #       315,303,290,277,262,248,239,226,219,208,198,187,174,164,155,146,140,132,123,115,106,99.8,91.8,86.3,80.3,73.5,64,55.5,43.8,34.8,138,131,
    #       238,304,298,391,362,430]
    lr1= [0,6.07,36.2,91.5,147,203,212,215,192,183,192,190,1528,1809,754,694,644,572,510,381,324,290,248,219,187,155,132,106,86.3,64,34.8,238,391,362,430]
    lr2= [
1250,1200,857,889,813,780,780,721,704,706,692,713,697,642,670,586,614,616,551,590,561,575,
        550,525,507,485,472,446,424,405,389,364,341,324,304,282,264,242,221,204,188,172,146,135,115,94,
        77,56.3,204,695,680,721,762,825,837,819,793,761,730,701,669,643,619,593,562,476,468,449,426,405,383,361,
        337,295,265,247,231,213,193,175,162,147,125,90.8,76.3,60,48.3,25, 100, 50]

    lr3=[1200, 1003,
690,541,534,496,476,453,425,400,375,355,320,299,287,268,244,219,197,172,158,138,119,98.3,76.3,49.3,207,719,740,718,727,750,757,785,778,737,691,702,701,692,678,638,618,610,587,571,553,526,512,472,480,464,452,434,409,388
,362,329,551,278,252,225,197,170,135,76.3,255,652,814,774,779
,755,787,725,764,708,702,699,690,693,682,659,636,611,587,557,533,517,506,482,460,444,429,414,395,
]
    t=0
    with open('l1y.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            if t%15 == 0:
                tp +=5
                lt.append(tp)
                lv.append(double(row[1]))
            t += 5



    ##########################################################


    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex=True)  # create the canvas for plotting


    ax1.plot(secta, sec, label='Event Arrival rate ' )
    ax1.plot(sectar, secr, label='Maximum Consumption rate' )

    ax2.plot(acqta, acq, label='sec µs')
    ax2.plot(acqtar, acqr, label='sec µs')
    ax3.plot(t15, lamda15, label='Issuer µs Arrival rate')
    ax3.plot(t1, lamda1, label='Maximum consumption rate \n (number of replicas)')

    ax4.plot(lt, lv, 'r', label='latency (ms)')
    ax4.plot(tr1, lr1, label='latency 2nd replica (ms)')
    ax4.plot(tr2, lr2, 'g', label='latency 3nd replica (ms)')
    ax4.plot(tr3, lr3, 'black', label='latency 4nd replica (ms)')

    ax1.set_ylabel('Security µs')
    ax2.set_ylabel('AcquirerBank')
    ax3.set_ylabel('IssuerBank')
    ax4.set_ylabel('End-to-end  \n latency (ms)')

    ax4.set_xlabel('Time (sec)')




    ax1.legend(fontsize='x-small')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    graf()