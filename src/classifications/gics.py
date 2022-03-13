from pathlib import Path
import pandas as pd
import json

from globals import *
from .classificator import Classificator, Category


class GICS(Classificator):
    """GICS class"""

    def __init__(self, schema_file=None):
        self.base().__init__(schema_file)
        self._categories = [Category.Region, Category.Sector]
        self._data_root = self._data_root / "gics"
        self._data_raw = self._data_root / "edited" / "GICS_map 2018.xlsx"

    def createSchemaDefinitions(self):
        for cat in self._categories:
            ret = self._createSchema(cat)
            with open(self._output_root / "GICS.json", "w") as file:
                json.dump(ret, file, indent=2)

    def _createSchema(self, cat: Category) -> dict:
        if cat is Category.Sector:
            return self._createSchemaSector()
        else:
            return self._createSchemaCountry()

    def _createSchemaCountry(self) -> dict:
        return {}

    def _createSchemaSector(self) -> dict:
        def tuplefy(row) -> list:
            lst = list(row)
            it = iter(lst)
            return list(zip(it, it))

        ret = {}

        df = pd.read_excel(
            self._data_raw,
            sheet_name=0,
            header=4,
            # usecols=[0, 1, 2, 3],
            skipfooter=2,
        )

        # Match data by creating new header, splitting the columns
        # of the old one in two new cells col_name_id:col_name
        header = tuplefy(df.columns.values)
        header = [[f"{e[0]}_id", e[0]] for e in header]
        header = [e for col_tuple in header for e in col_tuple]
        header_map = dict(zip(list(df.columns.values), header))
        df.rename(columns=header_map, inplace=True)

        df = df.dropna(thresh=2)  # drop detailed explanations

        # Make _id columns int64
        floaties = df.select_dtypes(include=["float64"])
        for col in floaties.columns.values:
            df[col] = df[col].astype(pd.Int64Dtype())

        # Make all string
        df = df.astype(pd.StringDtype())

        # print(df.head(20).to_string())

        header = tuplefy(df.columns.values)
        template = [None] * len(header)

        print(f"{header}\n----")
        col = header[0][1]
        # ret = {col: {}}  # "Sectors":{}
        for _, row in df.iterrows():
            r = tuplefy(row)
            for i, e in enumerate(r):
                if not pd.isna(e[0]):
                    template[i] = e
            print(f"{template}")
            d = ret
            for i, t in enumerate(template):
                col = header[i][1]  # 'Sector', 'Industry Group', ...
                d[col] = d.get(col, {})
                d[col][t[0]] = d[col].get(t[0], {})
                d[col][t[0]]["descr"] = t[1]
                d = d[col][t[0]]
        return ret
