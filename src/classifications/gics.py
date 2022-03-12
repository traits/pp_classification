from pathlib import Path
from globals import *
from .classificator import Classificator, Category


class GICS(Classificator):
    """GICS class"""

    def __init__(self, schema_file=None):
        self.base().__init__(schema_file)
        self._categories = [Category.Region, Category.Sector]
        self._data_root = self._data_root / "gics"
        self._data_raw = {"Sector": self._data_root / "GICS_map 2018.xlsx"}

    def createSchemaDefinitions(self) -> dict:
        for cat in self._categories:
            self._createSchema(cat)

    def _createSchema(self, cat: Category) -> dict:
        pass
