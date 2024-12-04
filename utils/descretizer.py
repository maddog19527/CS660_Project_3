import pandas as pd

"""
Converts fields with continuous variables to discrete catagories.

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