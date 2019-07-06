from matplotlib import pyplot as plt
import pandas as pd
import random
from itertools import count
from matplotlib.animation import FuncAnimation




def main():
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

if __name__ == "__main__":
    main()