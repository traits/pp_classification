import pandas as pd
import matplotlib.pyplot as plt

from globals import *

holding_data = (
    directories["stocks"]
    / "IE00BK5BQT80"
    / "Holdings details - FTSE All-World UCITS ETF - (USD) Accumulating - 3_11_2022.xlsx"
)
percent_column = "% of market value"
ticker_column = "Ticker"
holding_column = "Holding name"


def showPie():
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
