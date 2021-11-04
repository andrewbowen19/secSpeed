# secSpeed/analysis.py

'''
Script that makes use of the output csv from our combineScraper module in order to analyse combine stats across conferences


'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

data_path = os.path.join("..", "data", "all_combine_stats.csv")
df = pd.read_csv(data_path)

print(df.head())

skill_players = df.loc[(df['Pos'] != "DL" ) | (df['Pos'] != "OL") |
                       (df['Pos'] != "OT") | (df['Pos'] != "K") |
                       (df['Pos'] != "DT")|(df['Pos'] != "DE")]
print(skill_players.head())

def plot_avg_by_conf(dataframe=df, event="40yd", savefig=False, skill_players_only=False):
    '''
    Plots bar chart of average value for a combine event by conference
    
    
    parameters:
        dataframe : pandas.DataFrame object (default all combine stats); combine stats
        event : str (default 40yd); combine event desired, must match one of the columns of df
    '''
#    Grabbing skill position players if desired -- also including CBs and safeties
    if skill_players_only:
        
        dataframe = dataframe.loc[(dataframe['Pos']=="WR") |\
                                  (dataframe['Pos']=="RB") |\
                                  (dataframe['Pos']=="TE") |\
                                  (dataframe['Pos']=="QB")]
        print(dataframe)
    df_grouped = dataframe.groupby('Conference')[event].mean()
    print(f"Event: {event}")
    print(df_grouped)
    
    plt.bar(df_grouped.index, df_grouped.values)
#    plt.ylim([4.6,4.85])
    plt.xlabel('Conference')
    plt.ylabel(event)
    plt.title(f"NFL Combine {event} by Conference")
#    plt.show()
    

def plot_40_vs_3cone(df=df):
    '''
    Creates scatter plot of 40-yard times vs 3 cone drill times
    '''
    f,ax = plt.subplots()
    ax.scatter( df['3Cone'], df['40yd'])#, c=df['Conference'])
    ax.set_title('NFL Combine 40yd vs 3cone')
    ax.set_xlabel('3-cone time [s]')
    ax.set_ylabel('40-yard time [s]')
    
    f.savefig(os.path.join("..", "plots", "combine-40yd-3cone.png"))
    plt.show()
    

if __name__=="__main__":
    combine_events = ["40yd", "Vertical",
                      "Bench", "Broad Jump",
                      "3Cone","Shuttle"]

    for e in combine_events:
#        Can change the df passed to our function to
        plot_avg_by_conf(df, e, False, True)
        print('---------------------------------')
        
        print('#########################\n#########################\n########################')
        print('SKILL PLAYERS:')
        plot_avg_by_conf(df,e, False, True)

    plot_40_vs_3cone(df)
    plt.show()
