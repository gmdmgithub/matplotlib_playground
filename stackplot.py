from matplotlib import pyplot as plt


def main():

    plt.style.use('fivethirtyeight')

    minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    player1 = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]
    player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4, 5]
    player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4, 4]

    labels = ['player1', 'player2', 'player3']
    colors = ['#6d904f', '#fc4f30', '#008fd5']

    plt.stackplot(minutes, player1, player2, player3,
                  labels=labels, colors=colors)

    plt.legend(loc=(0.07, 0.7))

    plt.title('Awesome plot')
    plt.tight_layout()

    plt.show()
    plt.savefig('plot-stack.png')


if __name__ == "__main__":
    main()
