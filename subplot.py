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

def witSubplot(oneFigure):
    plt.style.use('seaborn')

    data = pd.read_csv('data3.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    
    if(oneFigure):
        # one figure two plots
        fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    else:
        # two separate plots 
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

    # plt.grid()

    plt.tight_layout()

    plt.show()

    # fig1.savefig('fig1.png')
    # fig2.savefig('fig2.png')

# Make some data
x_2 = np.linspace(-2, 2, 1000)

# Challenge: Write the g(x) function and the dg(x) function in Python?
def g(x):
    return x**4 - 4*x**2 + 5

def dg(x):
    return 4*x**3 - 8*x

# Gradient Descent as a Python Function
def gradient_descent(derivative_func, initial_guess, multiplier=0.02, precision=0.0001, 
                    max_iter=400):
    new_x = initial_guess
    x_list = [new_x]
    slope_list = [derivative_func(new_x)]

    for n in range(max_iter):
        previous_x = new_x
        gradient = derivative_func(previous_x)
        new_x = previous_x - multiplier * gradient

        step_size = abs(new_x - previous_x)
        x_list.append(new_x)
        slope_list.append(derivative_func(new_x))

        if step_size < precision:
            break
    return new_x, x_list, slope_list

def plotGradientDescent():
    # Calling gradient descent function
    local_min, list_x, deriv_list = gradient_descent(derivative_func=dg, initial_guess= 0)

    # Plot function and derivative and scatter plot side by side

    plt.figure(figsize=[15, 5])

    # 1 Chart: Cost function
    plt.subplot(1, 2, 1)

    plt.xlim(-2, 2)
    plt.ylim(0.5, 5.5)

    plt.title('Cost function', fontsize=17)
    plt.xlabel('X', fontsize=16)
    plt.ylabel('g(x)', fontsize=16)

    plt.plot(x_2, g(x_2), color='blue', linewidth=3, alpha=0.8)
    plt.scatter(list_x, g(np.array(list_x)), color='red', s=100, alpha=0.6)

    # 2 Chart: Derivative
    plt.subplot(1, 2, 2)

    plt.title('Slope of the cost function', fontsize=17)
    plt.xlabel('X', fontsize=16)
    plt.ylabel('dg(x)', fontsize=16)
    plt.grid()
    plt.xlim(-2, 2)
    plt.ylim(-6, 8)

    plt.plot(x_2, dg(x_2), color='skyblue', linewidth=5, alpha=0.6)
    plt.scatter(list_x, deriv_list, color='red', s=100, alpha=0.5)

    plt.show()
    plt.savefig('plot-gradient-descent.png')

def main():
    # basicNoSubPlot()
    # witSubplot(True)
    plotGradientDescent()

if __name__ == "__main__":
    main()

