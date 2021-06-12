"""
Script for model evaluation using benchmark metrics.
"""
# Import necessary libraries
import json
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_predict, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score
from param import Params

# Create file path to store metrics of the evaluated model.
Params.metrics.mkdir(parents=True, exist_ok=True)

# Load in test data for evaluation.
X_test = pd.read_csv(str(Params.features / 'test_features.csv'))
y_test = pd.read_csv(str(Params.features / 'test_target.csv'))

# Load in pre-trained model.
model = joblib.load(open(
    str(Params.models / 'model.joblib'), 'rb'
))

# Peform predictions on the model.
pred = cross_val_predict(
    model, X_test, y_test.to_numpy().ravel(), cv=3, n_jobs=-1, verbose=1
)

# Calculate metrics
prec = precision_score(y_test, pred)
rec = recall_score(y_test, pred)
con_mat = pd.DataFrame(
    confusion_matrix(y_test, pred),
    index=pd.MultiIndex.from_product(
        [['Actual'], ['No', 'Yes']]
    ),
    columns=pd.MultiIndex.from_product(
        [['Predicted'], ['No', 'Yes']]
    )
)
res = cross_val_score(
    model, X_test, y_test.to_numpy().ravel(), scoring='accuracy', cv=10,
    n_jobs=-1
)
acc = accuracy_score(y_test, pred)
ave_acc = np.mean(res)

# Store results of the metrics in the file path.
with open(str(Params.metrics / 'metrics.json'), 'w') as outfile:
    json.dump(
        dict(zip(['Accuracy', 'Average Accuracy', 'Precision', 'Recall'],
        [round(acc, 3), round(ave_acc, 3), round(prec, 3), round(rec, 3)])), outfile
    )

# Store confusion matrix in a csv file.
con_mat.to_csv(
    str(Params.metrics / 'confusion_matrix.csv')
)
