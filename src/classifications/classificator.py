from abc import ABC, abstractmethod
from pathlib import Path
from enum import IntEnum
from globals import *


class Category(IntEnum):
    Region = 1
    Sector = 2


class Classificator(ABC):
    """Classificator base class"""

    def base(self):
        return super(type(self), self)

    def __init__(self, schema_file=None):
        self._categories = []
        self._data_root = directories["classifications"]

    def categories(self) -> list:
        return self._categories

    @abstractmethod
    def createSchemaDefinitions(self) -> dict:
        pass
