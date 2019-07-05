from matplotlib import pyplot as plt


def simplePie():
    plt.style.use('fivethirtyeight')

    slices = [20, 30, 10, 30]
    labels = ['good', 'enough', 'better', 'very good']
    colors = ['blue', 'green', 'red', '#e5ae37']

    plt.pie(slices, labels=labels, colors=colors,
            wedgeprops={'edgecolor': 'black'})

    plt.title('Some data')

    # plt.legend()

    plt.tight_layout()
    plt.savefig('plot-piechart.png')
    plt.show()


def programLangsPie():
    plt.style.use('fivethirtyeight')

    slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097]
    labels = ['JavaScript', 'HTML/CSS', 'SQL',
              'Python', 'Java', 'Bash/Shell/PowerShell', 'C#']
    explode = [0, 0, 0, 0.05, 0, 0, 0]

    plt.pie(slices, labels=labels, explode=explode, shadow=True,
            startangle=45, autopct='%1.1f%%', # set percentage on the piechart
            wedgeprops=dict(edgecolor='black', width=0.7))#made dict from values - nice, adding with we get donut!

    plt.title('Language popularity')

    # plt.legend()

    plt.tight_layout()
    plt.savefig('plot-piechart-lp.png')
    plt.show()


def main():
    # simplePie()
    programLangsPie()


if __name__ == "__main__":
    main()
