import pandas as pd


def detect_outliers_iqr(data, column):
    """Detects outliers in the given column using the IQR method."""

    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

"""
Converts fields with continuous variables to discrete categories.

fields = {
    'column_name': ['bin_1','bin_2','bin_3','bin_4'],
    ...
}
"""
def discretize(dataFrame: pd.DataFrame, fields: dict):
    result = dataFrame.copy()
    for field, labels in fields.items():
        result[field] = pd.cut(dataFrame[field], bins=len(labels), labels=labels)
    
    return result


from skopt.plots import plot_objective, plot_histogram, plot_convergence, plot_gaussian_process
import matplotlib.pyplot as plt
def optimizationResults(opt):
    ax = plot_objective(
                result=opt.optimizer_results_[0],
                n_minimum_search=int(1e8)
                )
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()
    return ax

'''
Utility for one-hot encoding catagorical fields
fields = ['field_1','field_2',...]
'''
def encode(dataFrame: pd.DataFrame, fields: list):
    result = dataFrame.copy()
    newColumns = {}

    for field in fields:
        for _, fieldValue in enumerate(result[field].unique()):
            hotColumn = str(field)+'_'+str(fieldValue)
            newColumns[hotColumn] = result[field].eq(fieldValue)
            newColumns[hotColumn] = [int(value) for value in newColumns[hotColumn]]
        
    newFrame = pd.DataFrame.from_dict(newColumns)
    result = pd.concat([result, newFrame], axis=1)

    toDrop = fields + [str(field)+'_nan' for field in fields]

    result = result.drop(columns=toDrop, errors='ignore')
    return result

