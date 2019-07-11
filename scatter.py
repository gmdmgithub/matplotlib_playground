from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def simple():
    x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
    y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
    colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

    return x, y, colors

def fileData():
    data = pd.read_csv('2019-05-31-data.csv')
    x = data['view_count']
    y = data['likes']
    colors = data['ratio']

    return x,y, colors

def main():
    plt.style.use('seaborn')

    # x, y, colors = simple()
    x, y, colors = fileData()

    # plt.figure(figsize=(10,6))
    plt.ylim(0,y.max)
    plt.xlim(0,x.max)

    plt.scatter(x, y, s=150, c=colors, edgecolor='black', cmap='Blues',
                alpha=0.75, linewidths=1)

    cbar = plt.colorbar()
    cbar.set_label('Like/Dislike Ratio')

    

    plt.xscale('log')
    plt.yscale('log')

    plt.title('Trending')
    plt.xlabel('Viewers')
    plt.ylabel('Likes')

    plt.tight_layout()

    plt.savefig('plot-skatter.png')
    plt.show()


if __name__ == "__main__":
    main()
