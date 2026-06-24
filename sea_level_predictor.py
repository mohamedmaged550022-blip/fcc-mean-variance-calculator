import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1: Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2: Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data', s=10)

    # 3: Create first line of best fit (using all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = pd.Series([i for i in range(1880, 2051)])
    line1 = res1.slope * years_extended1 + res1.intercept
    plt.plot(years_extended1, line1, color='red', label='Fits all data (1880-2050)')

    # 4: Create second line of best fit (from year 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended2 = pd.Series([i for i in range(2000, 2051)])
    line2 = res2.slope * years_extended2 + res2.intercept
    plt.plot(years_extended2, line2, color='green', label='Fits recent data (2000-2050)')

    # 5: Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
