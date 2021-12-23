# secSpeed/combine.py

'''
Script to scrape NFL combine stats from Pro-FootballReference.com and compare 40-yard dash results between conferences

NFL Combine stats pulled from here: https://www.pro-football-reference.com/draft/2021-combine.htm
'''

import pandas as pd
import numpy as np
import os


class combineScraper(object):

    def __init__(self):
        self.conferences = {  #SEC
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
                   # Big 12
                   "Big 12": ["Baylor", "Iowa St.",
                              "Kansas", "Kansas St.",
                              "Oklahoma St.", "TCU",
                              "Texas Tech", "West Virgina",
                              "Texas", "Oklahoma"],
                   # Pac 12
                   "Pac-12": ["Arizona", "Arizona St.",
                              "California", "UCLA",
                              "Colorado", "Oregon",
                              "Oregon St.", "USC",
                              "Stanford", "Utah",
                              "Washington", "Washington St."]
                    }
                    

    def get_combine_stats(self, year, save_csv=False):
        '''
        Scrapes PFR for combine statistics per player for each year

        paramters:
            year : int or str; combine year for which statistics are desired

        returns:
            df : pandas.DataFrame object; contains combine statistics for each participant
        '''
        url = f"https://www.pro-football-reference.com/draft/{year}-combine.htm"
        df = pd.read_html(url)[0]
        
        # Cleaning df & determining conference for each player
        df = df.loc[df['Player'] != "Player"]
        df['Conference'] = df['School'].apply(self.determine_conference)
            
        if save_csv:
            df.to_csv(os.path.join("..", "data",f"combine_stats-{year}.csv"), index=False)
        
        print(df.head())
        
        return df
        
    def determine_conference(self,school):
        '''
        Determines conference of player based on school

        parameters
        '''
        if school in self.conferences['SEC']:
            return "SEC"
        elif school in self.conferences['ACC']:
            return "ACC"
        elif school in self.conferences['Big Ten']:
            return "Big Ten"
        elif school in self.conferences['Big 12']:
            return "Big 12"
        elif school in self.conferences['Pac-12']:
            return "Pac-12"
        else:
            return "Non Power-5"
            
    def get_all_combines(self, start=2010, end=2021,save_csv=True):
        '''
        Uses class method self.get_combine_stats to produce 
        
        parameters:
            start, end : int, default 2021 & 2010; start and end year of time range for which combine data should be pulled
            save_csv : boolean, default True; if True, save output dataframe as csv file in data directory

        returns:
            df : pd.DataFrame; contains combine event results for all players from start to end
        '''
        dfs = []
        for y in range(int(end), int(start), -1):
            print(f"Combine year: {y}")
            dfs.append(self.get_combine_stats(y, False))
            print('---------------------------------------')
            
        df = pd.concat(dfs)

        if save_csv:
            df.to_csv(os.path.join("..", "data", f'all_combine_stats.csv'), index=False)
        
        return df

if __name__=="__main__":
    # Get data for all combines 2010 - 2021
    df = combineScraper().get_all_combines()

