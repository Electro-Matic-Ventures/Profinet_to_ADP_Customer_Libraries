"""
    generates background color table
"""

from typing import Tuple
from constants_table_row import ConstantsTableRow
from project_constants import DATA_TYPE, PATH


class GenerateBackgroundColors:
    """
        generates background color table
    """
    __COLORS = [
        "BLACK",
        "RED",
        "GREEN",
        "YELLOW"
    ]
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """
            @return Tuple[ConstantsTableRow, ...]
        """
        table = []
        i = 1
        for color in GenerateBackgroundColors.__COLORS:
            table_row = ConstantsTableRow(
                name= f'BACKGROUND_COLOR_{color}',
                path= PATH,
                data_type= DATA_TYPE,
                value= i,
                comment= ""
            )
            table.append(table_row)
            i += 1
        return tuple(table)
    