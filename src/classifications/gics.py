from pathlib import Path
import pandas as pd

from globals import *
from .classificator import Classificator, Category


class GICS(Classificator):
    """GICS class"""

    def __init__(self, schema_file=None):
        self.base().__init__(schema_file)
        self._categories = [Category.Region, Category.Sector]
        self._data_root = self._data_root / "gics"
        self._data_raw = self._data_root / "edited" / "GICS_map 2018.xlsx"

    def createSchemaDefinitions(self) -> dict:
        for cat in self._categories:
            self._createSchema(cat)

    def _createSchema(self, cat: Category) -> dict:
        ret = {}

        if cat is Category.Sector:
            df = pd.read_excel(
                self._data_raw,
                sheet_name=0,
                header=4,
                # usecols=[0, 1, 2, 3],
                skipfooter=2,
            )

            # Match data by creating new header, splitting the columns
            # of the old one in two new cells col_name_id:col_name
            header = list(df.columns.values)
            it = iter(header)
            header = list(zip(it, it))
            header = [[f"{e[0]}_id", e[0]] for e in header]
            header = [e for col_tuple in header for e in col_tuple]
            header_map = dict(zip(list(df.columns.values), header))
            df.rename(columns=header_map, inplace=True)

            print(df.head(10).to_string())

        else:
            pass
        return ret
