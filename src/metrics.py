import numpy as np

def calculate_mape(y_true, y_pred):
    """
    Mean Absolute Percentage Error (MAPE) есептеу функциясы.
    Формула: mean(|(y_true - y_pred) / y_true|) * 100
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return mape