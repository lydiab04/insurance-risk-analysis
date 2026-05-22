import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def missing_values(df):
    """
    Returns missing value summary.
    """

    missing = df.isnull().sum()
    percent = (missing / len(df)) * 100

    return pd.DataFrame({
        "Missing Values": missing,
        "Percentage": percent
    }).sort_values(by="Percentage", ascending=False)


def plot_histogram(df, column):
    """
    Plot histogram for numerical feature.
    """

    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()


def plot_boxplot(df, column):
    """
    Plot boxplot for outlier detection.
    """

    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()


def correlation_matrix(df, numerical_cols):
    """
    Plot correlation matrix.
    """

    plt.figure(figsize=(12, 8))

    corr = df[numerical_cols].corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")
    plt.show()