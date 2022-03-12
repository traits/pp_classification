from .classificator import Classificator, Category


class ICB(Classificator):
    """ICB class"""

    def __init__(self, schema_file=None):
        self.base().__init__(schema_file)
        self._categories = [Category.Region, Category.Sector]
