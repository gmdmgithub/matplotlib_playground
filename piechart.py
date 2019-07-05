from matplotlib import pyplot as plt

def main():

    plt.style.use('fivethirtyeight')
    
    slices = [20,30,10,40]

    plt.pie(slices)

    plt.title('Some data')

    plt.legend()

    plt.tight_layout()
    plt.savefig('plot-piechart.png')
    plt.show()

if __name__ == "__main__":
    main()