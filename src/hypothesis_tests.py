import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, chi2_contingency


def t_test_groups(df: pd.DataFrame, group_col: str, value_col: str, group_a: str, group_b: str) -> dict:
    """
    Performs a Welch's independent two-sample t-test between two groups.
    Safely drops missing values and handles unequal group variances.
    """
    # 1. Isolate target groups and drop missing data
    a = df[df[group_col] == group_a][value_col].dropna()
    b = df[df[group_col] == group_b][value_col].dropna()

    # 2. Guard against insufficient sample sizes
    if len(a) < 2 or len(b) < 2:
        return {
            "error": f"Insufficient sample size for testing. Group A ({group_a}) count: {len(a)}, Group B ({group_b}) count: {len(b)}"
        }

    # 3. equal_var=False executes Welch's T-Test (essential for unequal group variances)
    stat, p = ttest_ind(a, b, equal_var=False, nan_policy='omit')

    return {
        "testing_feature": value_col,
        "group_a": group_a,
        "group_b": group_b,
        "mean_group_a": float(np.round(a.mean(), 4)),
        "mean_group_b": float(np.round(b.mean(), 4)),
        "test_statistic": float(np.round(stat, 4)),
        "p_value": float(p) if not np.isnan(p) else None,
        "statistically_significant": "Yes" if p < 0.05 else "No"
    }


def chi_square_test(df: pd.DataFrame, col1: str, col2: str) -> dict:
    """
    Performs a Chi-Square test of independence between two categorical variables.
    """
    # 1. Construct the cross-tabulation table
    contingency = pd.crosstab(df[col1], df[col2])

    # 2. Guard against entirely empty cross-tabs
    if contingency.size == 0:
        return {"error": f"One or both categorical columns ({col1}, {col2}) contain no data blocks."}

    # 3. Calculate metrics
    chi2, p, dof, expected = chi2_contingency(contingency)

    return {
        "variables_evaluated": f"{col1} vs {col2}",
        "chi2_statistic": float(np.round(chi2, 4)),
        "p_value": float(p) if not np.isnan(p) else None,
        "degrees_of_freedom": int(dof),
        "statistically_significant": "Yes" if p < 0.05 else "No"
    }