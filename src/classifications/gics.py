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
        with open(self._data_root / "meta.json", "r") as f:
            self._meta = json.load(f)
            self._data_raw = {}
            self._data_raw["EN"] = self._data_root / "edited" / "GICS_map 2018.xlsx"
            self._data_raw["DE"] = (
                self._data_root / "edited" / "GICS_map 2018_German.xlsx"
            )
        self._output_root = self._output_root / "GICS"

    def createSchemaDefinitions(self):
        self._output_root.mkdir(parents=True, exist_ok=True)
        for cat in self._categories:
            self._createSchema(cat)

    def _createSchema(self, cat: Category) -> dict:
        if cat is Category.Sector:
            self._createSchemaSectors()
        else:
            self._createSchemaCountries()

    def _createSchemaCountries(self):
        pass

    def _createSchemaSectors(self):
        self._createLangSectors("EN", True)
        self._createLangSectors("DE")

    def _createLangSectors(self, lang, export_sectors=False):
        def tuplefy(row) -> list:
            lst = list(row)
            it = iter(lst)
            return list(zip(it, it))

        df = pd.read_excel(
            self._data_raw[lang],
            sheet_name=0,
            header=4,
            # usecols=[0, 1, 2, 3],
            skipfooter=2,
        )

        # Match data by creating new header, splitting the columns
        # of the old one in two new cells col_name_id:col_name
        header = tuplefy(df.columns.values)

        i18n = {
            "categories": dict(
                zip(self._meta["categories"], [n for n, m in list(header)])
            )
        }

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

        # print(f"{header}\n----")
        col = header[0][1]
        schema = {}
        i18n["codes"] = {}
        for _, row in df.iterrows():
            r = tuplefy(row)
            for i, e in enumerate(r):
                if not pd.isna(e[0]):
                    template[i] = e
            # print(f"{template}")
            d = schema
            for i, t in enumerate(template):
                d[t[0]] = d.get(t[0], {})
                i18n["codes"][t[0]] = t[1]
                d = d[t[0]]

            # Be careful with encoding here
            if export_sectors:
                with open(self._output_root / f"sectors.json", "w+b") as file:
                    s = json.dumps(schema, indent=2, ensure_ascii=False).encode("utf-8")
                    file.write(s)
            with open(self._output_root / f"{lang}.json", "w+b") as file:
                s = json.dumps(i18n, indent=2, ensure_ascii=False).encode("utf-8")
                file.write(s)
