from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

def standadReader():
    with open('data2.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        language_counter = Counter()
        # row = next(csv_reader)
        # print(row['LanguagesWorkedWith'].split(";"))

        for row in csv_reader:
            language_counter.update(row['LanguagesWorkedWith'].split(";"))
    
    # print(language_counter)
    # print(language_counter.most_common(10))

    languages = []
    popularity = []
    for item in language_counter.most_common(12):
        languages.append(item[0])
        popularity.append(item[1])

    return languages, popularity

def pandasWay():
    data = pd.read_csv('data2.csv')

    ids = data['Responder_id']
    lang_answers = data['LanguagesWorkedWith']
    
    language_counter = Counter()
    for answer in lang_answers:
        language_counter.update(answer.split(";"))

    languages = []
    popularity = []
    for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])

    return languages, popularity

def main():

    plt.style.use('fivethirtyeight')
    
    languages, popularity = pandasWay() #standadReader()

    print(languages.reverse(), popularity.reverse())
    
    plt.barh(languages, popularity)


    # plt.ylabel('Languages')
    plt.xlabel('Popularity')
    plt.title('Popularity of programming')

    plt.legend()

    plt.tight_layout()
    plt.savefig('plot-lang-pop.png')
    plt.show()

if __name__ == "__main__":
    main()