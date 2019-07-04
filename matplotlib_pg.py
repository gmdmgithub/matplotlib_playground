from matplotlib import pyplot as plt
import numpy as np

def main():
    # plt.xkcd() #sketch-style drawing mode

    plt.style.use('fivethirtyeight')
    # plt.style.use('ggplot')

    ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

    x_indexes = np.arange(len(ages_x)) # using numpy lib create indexes to give some shift for a barchar
    width = 0.4 # without shift bars will overlaps

    py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 
                65998, 70003, 70000, 71496, 75370, 83640, 84666,
                84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 
                100771, 104708, 108423, 101407, 112542, 122870, 120000]
    
    js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 
                56373, 62375, 66674, 68745, 68746, 74583, 79000,
                78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 
                100000, 91660, 99240, 108000, 105000, 104000]

    # plt.plot(ages_x, py_dev_y,'d--r', label='Python')#format string used '[marker][line][color]'
    plt.bar(x_indexes, py_dev_y, width=width, label='Python')#format string used '[marker][line][color]'

    # plt.plot(ages_x, js_dev_y, label='JavaScript', color='#444444', marker='o', linestyle='dashed',
    #     linewidth=2, markersize=5)#better idea - format string

    plt.bar(x_indexes+width+0.05, js_dev_y, width=width, label='JavaScript')
    
    plt.xticks(ticks=x_indexes, labels=ages_x)

    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.title('Median Salary (USD) by Age')

    plt.legend()

    plt.tight_layout()
    # plt.grid(True)

    # because of arrange the data we need to rearrange ticks of the label x

    

    print(plt.style.available)

    plt.savefig('plot.png')

    plt.show()

if __name__ == "__main__":
    main()