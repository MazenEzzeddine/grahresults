# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # Call histogram() function that returns histogram data
    np_array = np.histogram([10, 3, 8, 9, 7], bins=[2, 4, 6, 8, 10])
    # Print the histogram output
    print("The output of histogram is : \n", np_array)

def plott():
    # Create histogram dataset
    hist_array, bin_array = np.histogram([4, 10, 3, 13, 8, 9, 7], bins=[2, 4, 6, 8, 10, 12, 14])

    # Set some configurations for the chart
    plt.figure(figsize=[10, 5])
    plt.xlim(min(bin_array), max(bin_array))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Edge Values', fontsize=20)
    plt.ylabel('Histogram Values', fontsize=20)
    plt.title('Histogram Chart', fontsize=25)

    # Create the chart
    plt.bar(bin_array[:-1], hist_array, width=0.5, color='blue')
    plt.hist()
    # Display t
    plt.show()



def cumhist():
    # data = [10, 2, 3, 40, 50, 10, 20, 20]
    #
    # plt.hist(data, bins=[0, 10, 20, 30, 40, 50, 100], density=True, cumulative=True, histtype='step')

    font = {#'family': 'Times New Roman',
            'weight': 'bold',
            'size': 10}

    mpl.rc('font', **font)

    fig, ax= plt.subplots()
    obs = [5.5, 2, 6, 1.3, 1.7, 1.8, 2, 3.1, 1.3, 6.5, 1.2, 1.1, 2.4, 2.8, 3.46, 2.5,  2.76, 3.2, 2.6, 1.6, 1.2, 1.3, 1.4, 2, 5.3,5, 1.99,4.8, 2, 3.2, 1.3, 1.9, 3.2,2.2, 1.1,
           6.2,1.9, 2.2, 4.3, 1.1, 1.3, 1.4, 3.9, 2, 1.7, 3.2, 2.2, 3, 2.8, 3.3, 3.21, 2.32, 1.7, 1.8, 1.9, 3.5, 1.8, 1.6, 4, 4.5, 5]
    #bins = [0.8, 1, 1.5,  2.5, 3,3.5]
    plt.hist(obs, bins=200, density=True, cumulative=True, histtype='step')
    plt.xlabel("Rebalancing time (sec)", fontdict= font)
    plt.ylabel("Probability", fontdict=font)

    plt.title("Rebalancing time cumulative distribution", fontdict=font)
    fix_hist_step_vertical_line_at_end(ax)


    plt.show()


def fix_hist_step_vertical_line_at_end(ax):
    axpolygons = [poly for poly in ax.get_children() if isinstance(poly, mpl.patches.Polygon)]
    for poly in axpolygons:
        poly.set_xy(poly.get_xy()[:-1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #
    # plott()

    cumhist()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
