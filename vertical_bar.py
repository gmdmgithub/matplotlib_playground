from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

def standadReader():
    with open('data2.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        language_counter = Counter()
        # row = next(csv_reader)
        # print(row['LanguagesWorkedWith'].split(";"))

        for row in csv_reader:
            language_counter.update(row['LanguagesWorkedWith'].split(";"))
    
    print(language_counter)

def main():

    plt.style.use('fivethirtyeight')
    
    standadReader()
    

    # plt.xlabel('Ages')
    # plt.ylabel('Median Salary (USD)')
    # plt.title('Median Salary (USD) by Age')

    # plt.legend()

    # plt.tight_layout()
    # plt.savefig('plot.png')
    # plt.show()

if __name__ == "__main__":
    main()