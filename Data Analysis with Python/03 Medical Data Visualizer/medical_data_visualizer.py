import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
# Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv("medical_examination.csv")
df.head()

# 2
# Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
df['overweight'] = (df["weight"] / (df["height"] / 100)**2 > 25).astype(int)
print(df.head())
# 3
# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
# Normalize cholesterol and glucose levels
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# print(df.head())

# 4
# Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # 5
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
                     var_name="variable", value_name="value")


    # 6
    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio", "variable", "value"])["value"].count().reset_index(name="total")
    

    # 7
    # Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().
    cat_plot = sns.catplot(x = "variable", y = "total", hue = "value", col = "cardio", data = df_cat,
                           kind="bar", height=5, aspect=1.2)


    # 8
    # Get the figure for the output and store it in the fig variable.
    fig = cat_plot.figure


    # 9
    # Do not modify the next two lines.
    fig.savefig('catplot.png')
    return fig





# 10
# Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # 11
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
        # diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
        # height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
        # height is more than the 97.5th percentile
        # weight is less than the 2.5th percentile
        # weight is more than the 97.5th percentile
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) &  (df['height'] <= df['height'].quantile(0.975)) & 
                      (df['weight'] >= df['weight'].quantile(0.025)) &  (df['weight'] <= df['weight'].quantile(0.975))]
    print(df_heat.head())

    # 12
    # Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr()

    # 13
    # Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    # Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    # Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", 
        cbar_kws={"shrink": 0.5}, ax=ax, square=True, linewidths=.5
    )


    # 16
    # Do not modify the next two lines.
    fig.savefig('heatmap.png')
    return fig
