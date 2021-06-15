"""
Utility methods script for notebooks
"""
import ppscore as pps
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import GridSearchCV


def clean_irrelevant_index(df, col_name, clean_item):
    """
    Utility function to remove irrelevant index features across a feature.
    --------------------
    Params:
        df : pandas DataFrame in question
        col_name : name of column in question
        clean_item : value to be dropped.
    --------------------
    Return:
        pandas Dataframe
    
    """
    # scan for specific item
    item = [clean_item]
    
    # single out item we are interested in
    drop_item = df[df[col_name].isin(item)]
    
    # drop our featured item index-wise
    df.drop(drop_item.index, axis=0, inplace=True)
    
    
    return df.head()
    pass


def pps_heatmap(df):
        
    """
    Utility function for calculating the Predictive Power Score and plotting a heatmap
    --------------------
    Args:
        df : Pandas DataFrame or Series object
    --------------------
    Returns:
            figure : Figure containing the predictive power score heatmap.
    """
    # Calculate pps matrix for the dataframe
    pps_mtrx = pps.matrix(df)
    pps_mtrx1 = pps_mtrx[['x', 'y', 'ppscore']].pivot(columns='x', index='y',
                                              values='ppscore')
    # Provide figure dimensions
    plt.figure(figsize=(30, 20))
    
    # Plot heatmap
    ax = sb.heatmap(pps_mtrx1, vmin=0, vmax=1, cmap="afmhot_r", linewidths=0.5,
                    annot=True)
    # Set labels and title
    ax.set_title("Predictive Power Score Heatmap")
    ax.set_xlabel("feature")
    ax.set_ylabel("target")
    return ax
    pass


def corr_heatmap(df, mask: bool):

    """
    Utility method to visualize pairwise correlation.
    --------------------
    Params:
        df : pandas DataFrame
    --------------------
    Returns:
        figure : Figure containing pairwaise correlation heatmap
    """
    
    # Set dimensions for the heatmap
    plt.figure(figsize=(30, 20))
    
    # Mask out duplicate values
    if mask is True:
      # Create mask
        mask = np.zeros_like(df.corr(), dtype=np.bool_)
        mask[np.triu_indices_from(mask)] = True
        
      # Generate heatmap with custom diverging color map
        ax = sb.heatmap(df.corr(), annot=True, cmap='cividis', linewidth=.5,
                   mask=mask)
    else:
        ax = sb.heatmap(df.corr(), annot=True, cmap='cividis')
    
    # set figure labels
    ax.set_title('Correlation Matrix')
    ax.set_xlabel('Feature')
    ax.set_ylabel('Target')
    plt.show()
    pass


def model_selection(est, scale, X, y, label, truth):
    """
    Utility function for trying out models.
    --------------------
    Params:
        Estimator: Base estimator for modelling.
        Scale: Preprocessing method to transform values to a certain scale.
        X, y: Train features and labels.
        Label: Test features
        Truth: Ground truth or test labels.
    --------------------
    Returns:
        Accuracy Score.
        Complete Classification Report.
        Confusion Matrix
    --------------------
    """
    # Chain estimator in a pipeline.
    pipe = Pipeline([('scale', scale),
                     ('estimator', est)], verbose=True)
    
    # Fit the pipeline to train data.
    pipe.fit(X, y)
    
    # Performing prediction on test data using pipeline.
    pred = pipe.predict(label)
    
    # Computing accuracy score.
    acc = accuracy_score(truth, pred)
    pre = precision_score(truth, pred)
    rec = recall_score(truth, pred)
    f1 = f1_score(truth, pred)
    print("Accuracy Score: {:2f}".format(acc))
    print("Precision Score: {:.2f}".format(pre))
    print("Recall Score: {:.2f}".format(rec))
    print("F1 Score: {:.2f}".format(f1))
    
    # Printing out classification report.
    print('Classification Report \n {} \n'.format(classification_report(
                                                    truth, pred
                                                )))
    
    # Creating the confusion matrix.
    con = pd.DataFrame(confusion_matrix(truth, pred),
                index=pd.MultiIndex.from_product(
                    [['Actual'], ['No', 'Yes']]
                ),
                columns=pd.MultiIndex.from_product(
                    [['Predicted'], ['No', 'Yes']]
                )
    )
    
    # Plotting the confusion matrix.
    plot_confusion_matrix(pipe, label, truth)
    
    return con
    pass


def param_optimization(estimator, params, X, y, cv:int, jobs: int):
    """
    Utility function to perform hyper-parameter optimization.
    --------------------
    Params:
        estimator : Base estimator to begin optimization
        params : Parameters to iterate for tuning
        X, y : Train data
        cv : Cross Validation folds
        jobs : number of jobs to run in parallel
    --------------------
    Returns:
        Best  estimator
        Best score that can be achieved by the best estimator
        Most optimum parameters to provide anticpated results
    """
    # Instantiate grid search estimator
    grd = GridSearchCV(
        estimator, params, scoring='accuracy', n_jobs=jobs, cv=cv, verbose=1
    )
    
    # Fit grid search estimator to data
    grd.fit(X, y)
    
    # Print out results
    print("Best Estimator: \n", grd.best_estimator_)
    print("Best Score: {0:.3f} \n".format(grd.best_score_))
    print("Best Params: \n", grd.best_params_)
    
    pass

