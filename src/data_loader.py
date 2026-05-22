import pandas as pd


def load_data(filepath):
    """
    Load insurance dataset.
    """

    df = pd.read_csv(filepath)

    return df