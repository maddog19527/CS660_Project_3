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

'''Discretized continuous features by binning them in equal width bins'''
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


