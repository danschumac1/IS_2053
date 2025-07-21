'''
2025-07-21
Author: Dan Schumacher
How to run:
   python .\src\final_projects\data_science_getting_started.py
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """Load the penguins dataset and drop missing values."""
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df

def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Return basic summary statistics of the dataset."""
    return df.describe()

def visualize_data(df: pd.DataFrame):
    """Generate a simple boxplot for body mass by sex."""
    sns.boxplot(x='sex', y='body_mass_g', data=df)
    plt.title('Body Mass by Sex')
    plt.show()

def main():
    df = load_and_clean_data('./data\penguins.csv')
    print("Summary Statistics:\n", summary_statistics(df))
    visualize_data(df)

if __name__ == "__main__":
    main()
