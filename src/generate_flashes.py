"""
    flash constants generator
"""


from typing import Tuple
from constants_table_row import ConstantsTableRow
from project_constants import DATA_TYPE, PATH


class GenerateFlashes:
    """
        flashes
    """
    __STATES = [
        "ON",
        "OFF"
    ]
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """
            @return Tuple[ConstantsTableRow, ...]
        """
        table = []
        i = 1
        for state in GenerateFlashes.__STATES:
            table_row = ConstantsTableRow(
                name = f'FLASH_{state}',
                path= PATH,
                data_type= DATA_TYPE,
                value= i,
                comment= ""
            )
            table.append(table_row)
            i += 1
        return tuple(table)