import numpy as np
from sklearn.metrics import (
    root_mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

def regression_metrics(y_true, y_pred):
    """Calculates evaluation metrics for continuous targets (Claim Severity)."""
    # Using the modern root_mean_squared_error to prevent deprecation crashes
    rmse = root_mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    return {
        "RMSE": float(np.round(rmse, 4)),
        "R2": float(np.round(r2, 4))
    }

def classification_metrics(y_true, y_pred):
    """Calculates evaluation metrics for discrete categories (Claim Occurrence)."""
    return {
        "Accuracy": float(np.round(accuracy_score(y_true, y_pred), 4)),
        "Precision": float(np.round(precision_score(y_true, y_pred, zero_division=0), 4)),
        "Recall": float(np.round(recall_score(y_true, y_pred, zero_division=0), 4)),
        "F1": float(np.round(f1_score(y_true, y_pred, zero_division=0), 4))
    }