from pathlib import Path

project_dir = Path(__file__).resolve().parent
data_dir = project_dir / "data" / "raw"
out_dir = project_dir / "_output"
holding_data = (
    data_dir
    / "Holdings details - FTSE All-World UCITS ETF - (USD) Accumulating - 3_11_2022.xlsx"
)


def f():
    print(f"{holding_data=}")


if __name__ == "__main__":
    f()
    print("script completed")
