import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

def main():

    plt.style.use('seaborn')

    data = pd.read_csv('data-date.csv')

    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)

    price_date = data['Date']
    price_close = data['Close']

    plt.plot_date(price_date, price_close, linestyle='solid')#linestyle - had to be set

    plt.gcf().autofmt_xdate()

    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()