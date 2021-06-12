"""
Script for performing feature extraction.
"""
# import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from param import Params

# Create file path to store extracted features.
Params.features.mkdir(parents=True, exist_ok=True)

# Load in train and test data
train_df = pd.read_csv(str(Params.data / 'train.csv'))
test_df = pd.read_csv(str(Params.data / 'test.csv'))

# Create function to extract and pre-process features.


def feature_extraction(dframe):
    """
    Utility function to extract features from dataset.
    """
    cols = ['criteria_3', 'target_type']
    diff = dframe.loc[:, cols]
    scale = StandardScaler()

    stand = pd.DataFrame(
        scale.fit_transform(diff), columns=cols
    )
    return stand


train_features = feature_extraction(train_df)
test_features = feature_extraction(test_df)

# Extract Target from dataset

train_target = train_df.loc[:, 'doubt_terrorism']
test_target = test_df.loc[:, 'doubt_terrorism']

# Save our preprocessed data to our features file path
train_features.to_csv(str(Params.features / 'train_features.csv'), index=None)
test_features.to_csv(str(Params.features / 'test_features.csv'), index=None)
train_target.to_csv(str(Params.features / 'train_target.csv'), index=None)
test_target.to_csv(str(Params.features / 'test_target.csv'), index=None)
