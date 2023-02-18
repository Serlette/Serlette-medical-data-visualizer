import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

df['overweight'] = np.where(df['weight'] / ((df['height'] * 0.01) ** 2) > 25, 1, 0)
#print(df.head())

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
#print(df)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.(
    df_cat = sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    #print(df_cat)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=df_cat)
    

    # Draw the catplot with 'sns.catplot()'
    #sns.catplot(x='variable', col='cardio', hue='value', kind='count', data=df_cat).set_axis_labels('variable', 'total')


    # Get the figure for the output
    fig = sns.catplot(x='variable', col='cardio', hue='value', kind='count', data=df_cat).set_axis_labels('variable', 'total')



    # Do not modify the next two lines
    #fig.savefig('catplot.png')
    #return fig
    plt.show()

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = round(df_heat.corr(), 2)
    #print(corr)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (8, 8))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, vmin=0, vmax=0.25, annot=True, fmt='.2f', annot_kws=None, linewidths=0, square=True, mask=mask, cbar_kws={'shrink': 70})


    # Do not modify the next two lines
    #fig.savefig('heatmap.png')
    #return fig
    plt.show()
draw_cat_plot()
draw_heat_map()
