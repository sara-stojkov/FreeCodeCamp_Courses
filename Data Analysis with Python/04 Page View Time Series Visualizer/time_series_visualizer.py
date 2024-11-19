import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

print(df.head())

def draw_line_plot():

    # Draw line plot

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['value'], label='Page Views', color='b')  # Use 'value' instead of 'int'
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.legend()
    plt.xticks(rotation=45)  
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    fig = plt.gcf()  

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    df_bar.plot(kind='bar', figsize=(12, 6))
    plt.title('Monthly Average Page Views')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()

    fig = plt.gcf()  

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    # Create year and month columns
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month_name().str[:3]
    
    # Create a figure with two subplots (side by side)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Plot Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1, hue='year', palette='coolwarm', legend=False)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Plot Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, hue='month', palette='coolwarm', legend=False)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Set correct month order and rotate labels for the second plot
    ax2.set_xticks(range(12))  # Set the number of ticks (12 months)
    ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

    # Make the layout tight so the plots are not cropped
    plt.tight_layout()

    # Save the figure
    fig.savefig('box_plot.png')
    plt.show()

    return fig

