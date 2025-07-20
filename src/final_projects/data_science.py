import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, pearsonr
import json


def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """Load the penguins dataset and drop missing values."""
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df


def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Return basic summary statistics of the dataset."""
    return df.describe()


def perform_ttest(df: pd.DataFrame, group_col: str, value_col: str, group1: str, group2: str):
    """Perform t-test between two groups."""
    group1_vals = df[df[group_col] == group1][value_col]
    group2_vals = df[df[group_col] == group2][value_col]
    t_stat, p_value = ttest_ind(group1_vals, group2_vals)
    return t_stat, p_value


def visualize_data(df: pd.DataFrame):
    """Generate visualizations for the dataset."""
    # Boxplot
    sns.boxplot(x='sex', y='body_mass_g', data=df)
    plt.title('Body Mass by Sex')
    plt.savefig('boxplot_body_mass_by_sex.png')
    plt.clf()

    # Scatterplot
    sns.scatterplot(x='flipper_length_mm', y='body_mass_g', hue='species', data=df)
    plt.title('Flipper Length vs Body Mass')
    plt.savefig('scatter_flipper_vs_bodymass.png')
    plt.clf()

    # Heatmap (advanced visualization)
    corr = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('heatmap_correlation.png')
    plt.clf()

    # Pairplot (advanced visualization)
    sns.pairplot(df, hue='species')
    plt.savefig('pairplot_penguins.png')
    plt.clf()


def additional_statistical_test(df: pd.DataFrame):
    """Perform Pearson correlation between flipper length and body mass."""
    correlation, p_value = pearsonr(df['flipper_length_mm'], df['body_mass_g'])
    return correlation, p_value


def save_results(summary_stats: pd.DataFrame, ttest_result: tuple, correlation_result: tuple):
    """Save analysis results to JSON."""
    results = {
        'summary_statistics': summary_stats.to_dict(),
        't_test': {'t_statistic': ttest_result[0], 'p_value': ttest_result[1]},
        'pearson_correlation': {'correlation': correlation_result[0], 'p_value': correlation_result[1]}
    }
    with open('analysis_results.json', 'w') as f:
        json.dump(results, f, indent=4)


def main():
    df = load_and_clean_data('penguins.csv')
    print("Summary Statistics:\n", summary_statistics(df))

    t_stat, p_val = perform_ttest(df, 'sex', 'body_mass_g', 'Male', 'Female')
    print(f"T-Test Result: t={t_stat:.3f}, p={p_val:.3f}")
    if p_val < 0.05:
        print("There is a significant difference in body mass between male and female penguins.")
    else:
        print("There is no significant difference in body mass between male and female penguins.")

    visualize_data(df)

    correlation, corr_pval = additional_statistical_test(df)
    print(f"Pearson Correlation between flipper length and body mass: r={correlation:.3f}, p={corr_pval:.3f}")

    save_results(summary_statistics(df), (t_stat, p_val), (correlation, corr_pval))


if __name__ == "__main__":
    main()
