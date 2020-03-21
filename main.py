import pandas as pd
import numpy as np
import matplotlib as mp


def main():
    full_data = pd.read_csv('full_data.csv')
    china = full_data.loc[full_data['location'] == 'China']
    uk = full_data.loc[full_data['location'] == 'United Kingdom']
    italy = full_data.loc[full_data['location'] == 'Italy']




if __name__ == "__main__":
    main()