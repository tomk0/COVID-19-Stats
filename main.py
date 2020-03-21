import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    full_data = pd.read_csv('full_data.csv')
    china = full_data.loc[full_data['location'] == 'China']
    uk = full_data.loc[full_data['location'] == 'United Kingdom']
    italy = full_data.loc[full_data['location'] == 'Italy']

    plt.plot(china['date'], china['total_cases'], color='red')
    plt.plot(uk['date'], uk['total_cases'], color='blue')
    plt.plot(italy['date'], italy['total_cases'], color='green')
    plt.show()


if __name__ == "__main__":
    main()