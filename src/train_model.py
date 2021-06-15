"""
Script to train model on preprocessed data.
"""
# Import necessary libraries.
import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from param import Params

# Create file path to store model artifacts from training script.
Params.models.mkdir(parents=True, exist_ok=True)

# Load in train data.
X_train = pd.read_csv(str(Params.features / 'train_features.csv'))
y_train = pd.read_csv(str(Params.features / 'train_target.csv'))

# Instantiate classifier
model = KNeighborsClassifier()

# Fit classifier to train data
model.fit(X_train, y_train.to_numpy().ravel())

# Save model in serialized format.
joblib.dump(model, str(Params.models / 'model.joblib'))
