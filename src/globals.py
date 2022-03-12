from pathlib import Path

directories = {}
directories["root"] = Path(__file__).resolve().parents[1]
directories["output"] = directories["root"] / "_output"
directories["data"] = directories["root"] / "data"
directories["stocks"] = directories["data"] / "stocks"
directories["classifications"] = directories["data"] / "classifications"
