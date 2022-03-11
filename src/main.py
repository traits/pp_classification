from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project_dir = Path(__file__).resolve().parents[1]
data_dir = project_dir / "data" / "raw"
out_dir = project_dir / "_output"
holding_data = (
    data_dir
    / "Holdings details - FTSE All-World UCITS ETF - (USD) Accumulating - 3_11_2022.xlsx"
)


def f():
    print(f"{holding_data=}")
    df = pd.read_excel(
        holding_data,
        # sheet_name=1,
        header=6,
        # usecols=[0, 1, 2, 3],
        skipfooter=2,
    )

    percent_column = "% of market value"
    ticker_column = "Ticker"
    holding_column = "Holding name"

    print(df[[ticker_column, holding_column, percent_column]].head(10))

    df[percent_column] = df[percent_column].str.replace("%", "")
    df[percent_column] = df[percent_column].astype(float)

    plt.pie(df[percent_column], labels=df[ticker_column])
    plt.show()


if __name__ == "__main__":
    f()
    print("script completed")
