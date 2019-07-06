from matplotlib import pyplot as plt
import pandas as pd

import numpy as np


def simple():

    ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

    # plt.hist(ages, bins=8, edgecolor='black') #automatically calculate bins

    bins = [20, 30, 40, 50, 60]

    return ages, bins


def fromFile():
    data = pd.read_csv('data_h.csv')

    ids = data['Responder_id']
    ages = data['Age']

    bins = [15, 20, 25, 30, 35, 40, 45, 50, 55, 65, 70]
    return ages, bins


def main():

    plt.style.use('fivethirtyeight')

    #data, bins = simple()
    data, bins = fromFile()

    #plt.hist(data, bins=bins, edgecolor='grey')  # beans defined

    plt.hist(data, bins=bins, edgecolor='grey', log=True)# logarithmic scale - good for small numbers

    plt.axvline(np.mean(data),color='red', label='Average age')

    plt.legend()

    plt.title('Ages of Respondents')
    plt.xlabel('Ages')
    plt.ylabel('Total Respondents')

    plt.tight_layout()

    plt.savefig('plot-hist.png')
    plt.show()


if __name__ == "__main__":
    main()
