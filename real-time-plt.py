from matplotlib import pyplot as plt
import pandas as pd
import random
from itertools import count
from matplotlib.animation import FuncAnimation

def fileReader():
    plt.style.use('fivethirtyeight')
    x_vals = []
    y_vals = []

    def animate(i):
        data = pd.read_csv('data_rt.csv')
        x_vals = data['x_value']
        y_vals1 = data['total_1']
        y_vals2 = data['total_2']
        plt.cla() # without it color will change
        plt.plot(x_vals, y_vals1, label="values 1")
        plt.plot(x_vals, y_vals2, label="values 2")
        plt.legend(loc=(-0.07,1.1))
        
        plt.title('Real time data plot')
        plt.xlabel('Time')
        plt.ylabel('Various data (stock)')
        
        plt.tight_layout()
    
    ani = FuncAnimation(plt.gcf(),animate, interval=1000)
    
    plt.show()

def simple():
    plt.style.use('fivethirtyeight')

    x_vals = []
    y_vals = []

    index = count()

    def animate(i):
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 10))
        plt.cla() # without it color will change
        plt.plot(x_vals, y_vals)
    
    ani = FuncAnimation(plt.gcf(),animate, interval=1000)

    plt.tight_layout()
    # plt.savefig('real-time.png')
    plt.show()

def main():
    # simple()
    fileReader()

if __name__ == "__main__":
    main()