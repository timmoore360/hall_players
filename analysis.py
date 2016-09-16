## Analyzing historical baseball data with the aim to identify what characteristics correlate best with being voted into the Hall of Fame.

## Questions to be addressed in the analysis below:
## 1. What players seem to have been missed by Hall of Fame voters?
## 2. What statistic categories do borderline Hall of Fame candidates perform best in?
## 3. Why might these players be excluded from the Hall of Fame?

import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

## Data Wrangling - read .csv files that are to be examined in dataframes
## create column name lists
hall_columns = ['playerID', 'yearID', 'votedBy', 'ballots', 'needed', 'votes', 'inducted', 'category', 'needed_note']

batting_columns = ['playerID', 'yearID', 'stint', 'teamID', 'lgID', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 
                   'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP']

pitching_columns = ['playerID', 'yearID', 'stint', 'teamID', 'lgID', 'W', 'L', 'G', 'GS', 'CG', 'SHO', 'SV', 'IPOuts', 'H Allowed', 
                    'ER', 'HR Allowed', 'BB Allowed', 'K', 'BAOpp', 'ERA', 'IBB', 'WP', 'HBP', 'BK', 'BFP', 'GF', 'R Allowed', 'SH', 
                    'SF', 'GIDP Induced']

## read in wanted .csv files 
## update the path variable to the location you have saved this data set

path = 

hall_of_fame = pd.read_csv(path + 'HallOfFame.csv', header=0, low_memory=False)

batting_regular_season = pd.read_csv(path + 'Batting.csv', header=0, low_memory=False)

pitching_regular_season = pd.read_csv(path + 'Pitching.csv', skiprows=1,names=pitching_columns,
                                      low_memory=False)
