import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y, label="Original Data", color='blue')

    # Create first line of best fit (all data)
    result1 = linregress(x, y)
    x_all = pd.Series(range(x.min(), 2051))
    y_linreg1 = result1.slope * x_all + result1.intercept
    plt.plot(x_all, y_linreg1, label="Best Fit (All Data)", color='green')

    # Create second line of best fit (Year > 2000)
    df_filtered = df[df["Year"] >= 2000]
    x_filtered = df_filtered["Year"]
    y_filtered = df_filtered["CSIRO Adjusted Sea Level"]
    result2 = linregress(x_filtered, y_filtered)
    x_extended = pd.Series(range(x_filtered.min(), 2051))
    y_linreg2 = result2.slope * x_extended + result2.intercept
    plt.plot(x_extended, y_linreg2, label="Best Fit (Year > 2000)", color='red')

    # Add labels, legend, and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    # plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
