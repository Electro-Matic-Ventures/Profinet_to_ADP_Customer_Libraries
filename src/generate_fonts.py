"""
    generate font constants table
"""


from typing import Tuple
from constants_table_row import ConstantsTableRow
from project_constants import PATH, DATA_TYPE

class GenerateFonts:
    """
        generate font entries for constants table
    """
    __FONT_WEIGHTS = [
        "NORMAL",
        "BOLD"
    ]
    __NORMAL_SIZES = [
        5,
        7,
        9,
        11,
        14,
        15,
        16,
        22,
        24,
        30,
        32,
        40
    ]
    __BOLD_SIZES = [
        5,
        11,
        14,
        15,
        16,
        22,
        30,
        32,
        40
    ]
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """
            @return Tuple[ConstantsTableRow, ...]
        """
        table = []
        i = 1
        sizes = GenerateFonts.__NORMAL_SIZES
        for weight in GenerateFonts.__FONT_WEIGHTS:
            if weight == 'bold':
                sizes = GenerateFonts.__BOLD_SIZES
            for size in sizes:
                table_row = ConstantsTableRow(
                    name = f'FONT_{weight}_{size}',
                    path = PATH,
                    data_type = DATA_TYPE,
                    value = i,
                    comment = ''
                )
                table.append(table_row)
                i += 1
        return tuple(table)
