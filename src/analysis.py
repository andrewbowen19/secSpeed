# secSpeed/analysis.py

'''
Script that makes use of the output csv from our combineScraper module
Analyzes NFL combine stats across conferences
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


data_path = os.path.join("..", "data", "all_combine_stats.csv")
df = pd.read_csv(data_path)

# For plotting by conference later
colordict = {'Non Power-5': '#000000',
             'ACC': '#013ca6', 'SEC': '#004b8d',
             'Big 12': '#ef483e', 'Big Ten': '#0088ce',
             'Pac-12': '#004b91'}
df['Color'] = df['Conference'].apply(lambda x: colordict[x])

# Pulling out only skill position players (non-lineman/linebackers/special teams)
skill_players = df.loc[(df['Pos'] != "DL" ) | (df['Pos'] != "OL") |
                       (df['Pos'] != "OT") | (df['Pos'] != "K") |
                       (df['Pos'] != "DT")|(df['Pos'] != "DE")]
print('Skill Players @ NFL Combine:')
print(skill_players.head())

def plot_avg_by_conf(dataframe=df, event="40yd", savefig=False, skill_players_only=False):
    '''
    Plots bar chart of average value for a combine event by conference
    
    parameters:
        dataframe : pandas.DataFrame object (default all combine stats); combine stats
        event : str (default 40yd); combine event desired, must match one of the columns of df
    '''
    # Grabbing skill position players if desired -- also including CBs and safeties
    if skill_players_only:
        
        dataframe = dataframe.loc[(dataframe['Pos']=="WR") |\
                                  (dataframe['Pos']=="RB") |\
                                  (dataframe['Pos']=="TE") |\
                                  (dataframe['Pos']=="QB")]
    df_grouped = dataframe.groupby('Conference')[event].mean()
    print(f"Event: {event}")
    print(df_grouped)
    f,ax = plt.subplots()
    ax.bar(df_grouped.index, df_grouped.values)
    ax.set_xlabel('Conference')
    ax.set_ylabel(event)

    if skill_players_only:
        title = f"NFL Combine {event} by Conference -- Skill Players"
    else:
        title = f"NFL Combine {event} by Conference"
    ax.set_title(title)

    if savefig:
        path = os.path.join('..', 'plots', f'bar_chart_{event}.pdf')
        f.savefig(path)
    print('---------------------------------')

def event_scatter(df=df, xlabel='3Cone', ylabel='40yd', savefig=False):
    '''
    Creates scatter plot of 2 combine events 

    parameters:
        df : pd.DataFrame; contains comin
    '''
    # Plot that jawn (seabornd)
    f, ax = plt.subplots()
    sns.scatterplot(data=df, x=xlabel, y=ylabel, hue='Conference')
    
    # Save that jawn
    if savefig:
        f.savefig(os.path.join("..", "plots", f"combine-{xlabel}-{ylabel}.png"))
    # plt.show()

def create_histogram(data=df, xlabel='40yd', savefig=True):
    '''Creates panel plot of histogram '''
    
    # Generating histogram plot for each conference
    f, axs = plt.subplots(nrows=6, ncols=1, sharex=True, gridspec_kw={"hspace": 0.0})
    
    for i, conf in enumerate(df['Conference'].unique()):
        print(i, conf)

        axs[i].hist(data[xlabel].loc[data['Conference']==conf],
                    bins=20, range=(4.15, 6.0))
        axs[i].set_ylabel(f"{conf}")

    # plt.tight_layout()
    axs[0].set_title(f"{xlabel} - All conferences")
        
        # Saving figure if desired
    if savefig:
        path = os.path.join("..", "plots", f"combine-{xlabel}-hist.png")
        f.savefig(path)
    plt.show()



if __name__=="__main__":
    # Creating plots for each event to cross-compare conferences
    combine_events = ["40yd", "Vertical",
                      "Bench", "Broad Jump",
                      "3Cone","Shuttle"]
    create_histogram()
    for e in combine_events:
        plot_avg_by_conf(df, e, True, False)
        
        print('SKILL PLAYERS:')
        plot_avg_by_conf(df,e, True, True)

        print('######################')
        print(f'Creating scatter plot: 40yd v {e}')
        event_scatter(df, '40yd', e, True)
    # plt.show()
