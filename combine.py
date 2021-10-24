# secSpeed/combine.py

'''
Script to scrape NFL combine stats from Pro-FootballReference.com and compare 40-yard dash results between conferences
'''

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

conferences = {  #SEC
                "SEC": ["Alabama", "Auburn",
                       "Arkansas","Florida",
                       "Georgia", "Kentucky",
                       "LSU", "Mississippi",
                       "Mississippi St.", "Missouri",
                       "South Carolina", "Tennessee",
                       "Texas A&M","Vanderbilt"],
               # B1G
               "Big Ten": ["Illinois", "Indiana",
                           "Iowa", "Maryland",
                           "Michigan", "Michigan St.",
                           "Minnesota", "Nebraska",
                           "Northwestern", "Ohio St.",
                           "Penn St.", "Purdue",
                           "Rutgers", "Wisconsin"],
               # ACC
               "ACC": ["Boston College", "Clemson",
                       "Duke", "Florida St.",
                       "Georgia Tech", "Louisville",
                       "Miami (FL)", "North Carolina",
                       "NC St.", "Pittsburgh",
                       "Syracuse", "Virgina",
                       "Virginia Tech", "Wake Forest",
                       "Notre Dame"],
               
               "Big 12": ["Baylor", "Iowa St.",
                          "Kansas", "Kansas St.",
                          "Oklahoma St.", "TCU",
                          "Texas Tech", "West Virgina",
                          "Texas", "Oklahoma"],
               
               "Pac-12": ["Arizona", "Arizona St.",
                          "California", "UCLA",
                          "Colorado", "Oregon",
                          "Oregon St.", "USC",
                          "Stanford", "Utah",
                          "Washington", "Washington St."]
                       
                }
                

def get_combine_stats(year, save_csv=False):
    '''
    Scrapes PFR for combine statistics per player for each year

    paramters:
        year : int or str; combine year for which statistics are desired

    returns:
        df : pandas.DataFrame object; contains combine statistics for each participant
    '''
    url = f"https://www.pro-football-reference.com/draft/{year}-combine.htm"
    df = pd.read_html(url)[0]
    
#    Cleaning df
    df = df.loc[df['Player'] != "Player"]
    
#    Determining Conference for eacxh player
    df['Conference'] = df['School'].apply(determine_conference)
        
    if save_csv:
        df.to_csv(f"combine_stats-{year}.csv", index=False)
    
    print(df.head())
    
    return df
    
def determine_conference(school):
    '''
    Determines conference of player based on school
    '''
    if school in conferences['SEC']:
        return "SEC"
        
    elif school in conferences['ACC']:
        return "ACC"
    elif school in conferences['Big Ten']:
        return "Big Ten"
    elif school in conferences['Big 12']:
        return "Big 12"
    elif school in conferences['Pac-12']:
        return "Pac-12"
    else:
        return "Non Power-5"
        
def get_all_combines():
#    looping through combine years to get one big df
    dfs = []
    for y in range(2021, 2010, -1):
        print(f"Combine year: {y}")
        dfs.append(get_combine_stats(y, False))
        print('---------------------------------------')
        
    df = pd.concat(dfs)
    
    print(df)
    df.to_csv(f'all_combine_stats.csv', index=False)
    
    return df

if __name__=="__main__":
#    Will need to run a groupby conference to finish this up
    get_all_combines()


