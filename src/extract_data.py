"""
Script to extract data from remote storage.
"""
# Import necessary libraries and dependecies
import os
import gdown
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from param import Params
import utils

# Generate random number
np.random.seed(42)
random = Params.random_state

# Create directories to store extracted data
Params.original.parent.mkdir(parents=True, exist_ok=True)
Params.data.mkdir(parents=True, exist_ok=True)

# Extract data from remote storage
gdown.download(
    os.environ.get('DATA'),
    str(Params.original), quiet=False
)

# Load extracted in pandas DataFrame
df = pd.read_excel(str(Params.original))

# Slicing data for Somalia
som_df = df.groupby(['country_txt']).get_group('Somalia').copy()

# Reset index to match length of data.
som_df.reset_index(drop=True, inplace=True)

# Drop null values.
som_df.dropna(axis=1, inplace=True)

# Rename features with descriptive names.
som_df.rename(columns={
    'iyear': 'year', 'imonth': 'month', 'iday': 'day',
    'country_txt': 'country_name', 'region_txt': 'region_name',
    'attacktype1': 'attack_type', 'attacktype1_txt': 'attack_name',
    'targtype1': 'target_type', 'targtype1_txt': 'target_name',
    'gname': 'group_name', 'weaptype1': 'weapon_type',
    'weaptype1_txt': 'weapon_name', 'crit1': 'criteria_1',
    'crit2': 'criteria_2', 'crit3': 'criteria_3',
    'doubtterr': 'doubt_terrorism', 'provstate': 'state',
    'ishostkid': 'hostage_kidnap'
}, inplace=True)

# Drop days and months with 0 due to their unknown nature
utils.clean_irrelevant_index(som_df, 'day', 0)
utils.clean_irrelevant_index(som_df, 'month', 0)

# Before 1997, instance where there is essentially no doubt as to whether the
# incident is an act of terrorism was recorded as -9
# so we need to change it to 0.
for index in som_df.index:
    if som_df.loc[index, 'doubt_terrorism'] == -9:
        som_df.loc[index, 'doubt_terrorism'] = 0

# Reset data index
som_df.reset_index(drop=True, inplace=True)

# Drop features that are irrelevant to the problem statement
irrelevant = ['dbsource', 'INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY',
              'eventid', 'country', 'country_name', 'region_name', 'region',
              'individual']

som_df.drop(irrelevant, axis=1, inplace=True)

# Split data to train and test by ration of 80% and 20 % respectively
df_train, df_test = train_test_split(som_df, test_size=0.2, random_state=0)

# Saving data in to newly created file paths
df_train.to_csv(str(Params.data / 'train.csv'), index=None)
df_test.to_csv(str(Params.data / 'test.csv'), index=None)
