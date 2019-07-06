from matplotlib import pyplot as plt
import pandas as pd


def simple():
    plt.style.use('fivethirtyeight')

    data = pd.read_csv('data3.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, dev_salaries, color='#444444',
             linestyle='--', label='All Devs')

    plt.plot(ages, py_salaries, label='Python')
    plt.plot(ages, js_salaries, label='JavaScript')

    overall_median = 57287

    plt.fill_between(ages, py_salaries, overall_median, where=(
        py_salaries > overall_median), interpolate=True,  alpha=0.2)

    # different color below the median

    plt.fill_between(ages, py_salaries, overall_median, where=(
        py_salaries < overall_median), color='red', interpolate=True,  alpha=0.2)
    plt.legend()

    plt.title('Median Salary (USD) by Age')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    plt.tight_layout()

    plt.show()


def betweenTwo():
    plt.style.use('fivethirtyeight')
    
    data = pd.read_csv('data3.csv')
    ages = data['Age']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, py_salaries, label='Python')
    plt.plot(ages, js_salaries, label='JavaScript')

    plt.fill_between(ages, py_salaries, js_salaries, where=(
        py_salaries > js_salaries), interpolate=True,  alpha=0.2, label="Above javascript")

    plt.fill_between(ages, py_salaries, js_salaries, where=(
        py_salaries < js_salaries), color='red', interpolate=True,  alpha=0.2, label="Below javascript")
    plt.legend()

    plt.title('Median Salary (USD) by Age')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    plt.tight_layout()

    plt.show()


def main():

    # simple()

    betweenTwo()


if __name__ == "__main__":
    main()
