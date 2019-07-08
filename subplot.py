from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def basicNoSubPlot():

    plt.style.use('seaborn')

    data = pd.read_csv('data3.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, py_salaries,linestyle=':',  label='Python')
    plt.plot(ages, js_salaries, linestyle='-.', label='JavaScript')

    plt.plot(ages, dev_salaries, color='#444444',
            linestyle='--', label='All Devs')

    plt.legend()

    plt.title('Median Salary (USD) by Age')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    plt.tight_layout()

    plt.show()

def witSubplot():
    plt.style.use('seaborn')

    data = pd.read_csv('data3.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    # fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    ax1.plot(ages, dev_salaries, color='#444444',
            linestyle='--', label='All Devs')

    ax2.plot(ages, py_salaries,linestyle=':',  label='Python')
    ax2.plot(ages, js_salaries, linestyle='-.',  label='JavaScript')

    ax1.legend()
    ax1.set_title('Median Salary (USD) by Age')
    ax1.set_ylabel('Median Salary (USD)')

    ax2.legend()
    ax2.set_xlabel('Ages')
    ax2.set_ylabel('Median Salary (USD)')

    plt.tight_layout()

    plt.show()

    # fig1.savefig('fig1.png')
    # fig2.savefig('fig2.png')

def main():
    # basicNoSubPlot()
    witSubplot()

if __name__ == "__main__":
    main()

