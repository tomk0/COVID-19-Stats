import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import matplotlib.dates as mdates
from datetime import datetime

def main():
    full_data = pd.read_csv('full_data.csv')
    
    china = full_data.loc[full_data['location'] == 'China']

    uk = full_data.loc[full_data['location'] == 'United Kingdom']
    uk['date'] = pd.to_datetime(uk['date'])
    uk.set_index('date', inplace=True)

    italy = full_data.loc[full_data['location'] == 'Italy']
    italy['date'] = pd.to_datetime(italy['date'])
    italy.set_index('date', inplace=True)

    month = mdates.MonthLocator()
    day = mdates.DayLocator()
    month_fmt = mdates.DateFormatter('%m')

    fig, ax = plt.subplots()
    ax.plot('date', 'adj_close', data=china['totla_cases'])
    ax.xaxis.set_major_locator(month)
    ax.xaxis.set_major_formatter(month_fmt)
    ax.xaxis.set_minor_locator(day)

    datemin = np.datetime64(full_data['date'][1], 'M')
    datemaz = np.datetime64(full_data['date'][-1], 'M') + np.timedelta64(1, 'M')
    ax.set_xlim(datemin, datemax)

    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

    fig.autofmt_xdate()

    plt.show()

    #plt.plot_date(china['date'], china['total_cases'], color='red')

    #plt.plot(uk['date'], uk['total_cases'], color='blue')
    #plt.plot(italy['date'], italy['total_cases'], color='green')
    # plt.show()




if __name__ == "__main__":
    main()