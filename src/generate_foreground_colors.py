"""
    generates foreground color table
"""

from typing import Tuple
from constants_table_row import ConstantsTableRow
from project_constants import DATA_TYPE, PATH


class GenerateForegroundColors:
    """
        generates foreground color table
    """
    __COLORS = [
        "BLACK",
        "RED",
        "GREEN",
        "YELLOW",
        "MIX_1",
        "MIX_2",
        "MIX_3",
        "MIX_4",
        "BLUE",
        "WHITE"
    ]
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """
            @return Tuple[ConstantsTableRow, ...]
        """
        table = []
        i = 1
        for color in GenerateForegroundColors.__COLORS:
            table_row = ConstantsTableRow(
                name= f'FOREGROUND_COLOR_{color}',
                path= PATH,
                data_type= DATA_TYPE,
                value= i,
                comment= ""
            )
            table.append(table_row)
            i += 1
        return tuple(table)
    