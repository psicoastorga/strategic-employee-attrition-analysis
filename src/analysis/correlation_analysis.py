# Archivo: src/analysis/correlation_analysis.py
# Análisis de correlación con la variable Attrition

import matplotlib.pyplot as plt

def attrition_correlations(df):

    cols = [
        "Attrition",
        "CareerMobility",
        "PromotionVelocity",
        "StagnationIndex",
        "LoyaltyRate"
    ]

    return df[cols].corr()


def plot_correlation_heatmap(df):

    corr = df[
        ["Attrition","CareerMobility","PromotionVelocity","StagnationIndex","LoyaltyRate"]
    ].corr()

    plt.imshow(corr, cmap="coolwarm")
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title("Correlation Heatmap")
    plt.show()
