from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# from indexes.gics import GICS
# from indexes.icb import ICB


project_dir = Path(__file__).resolve().parents[1]
out_dir = project_dir / "_output"
data_dir = project_dir / "data" / "raw"
classification_dir = data_dir / "classifications"
stock_dir = data_dir / "stock"
holding_data = (
    stock_dir
    / "IE00BK5BQT80"
    / "Holdings details - FTSE All-World UCITS ETF - (USD) Accumulating - 3_11_2022.xlsx"
)
percent_column = "% of market value"
ticker_column = "Ticker"
holding_column = "Holding name"


def f():
    print(f"{holding_data=}")
    df = pd.read_excel(
        holding_data,
        # sheet_name=1,
        header=6,
        # usecols=[0, 1, 2, 3],
        skipfooter=2,
    )

    df[percent_column] = df[percent_column].str.replace("%", "")
    df[percent_column] = df[percent_column].astype(float)

    print(df[[ticker_column, holding_column, percent_column]].head(10))

    plt.pie(df[percent_column], labels=df[ticker_column])
    plt.show()


if __name__ == "__main__":
    # g = GICS()
    # i = ICB()

    f()
    print("script completed")
