# secSpeed/analysis.py

'''
Script that makes use of the output csv from our combineScraper module
Analyzes NFL combine stats across conferences
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

data_path = os.path.join("..", "data", "all_combine_stats.csv")
df = pd.read_csv(data_path)

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
    

def plot_40_vs_3cone(df=df, savefig=False):
    '''
    Creates scatter plot of 40-yard times vs 3 cone drill times

    parameters:
        df : pd.DataFrame; contains comin
    '''
    # Plot that jawn
    f,ax = plt.subplots()
    ax.scatter( df['3Cone'], df['40yd'])
    ax.set_title('NFL Combine 40yd vs 3cone')
    ax.set_xlabel('3-cone time [s]')
    ax.set_ylabel('40-yard time [s]')
    
    # Save that jawn
    if savefig:
        f.savefig(os.path.join("..", "plots", "combine-40yd-3cone.png"))
    plt.show()
    

if __name__=="__main__":
    # Creating plots for each event to cross-compare conferences
    combine_events = ["40yd", "Vertical",
                      "Bench", "Broad Jump",
                      "3Cone","Shuttle"]

    for e in combine_events:
        plot_avg_by_conf(df, e, True, False)
        
        print('SKILL PLAYERS:')
        plot_avg_by_conf(df,e, True, True)
    plot_40_vs_3cone(df, True)
    plt.show()
