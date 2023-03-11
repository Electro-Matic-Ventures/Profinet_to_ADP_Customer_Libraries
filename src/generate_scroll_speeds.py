"""
    generate scroll speed entries
"""


from typing import Tuple
from constants_table_row import ConstantsTableRow
from project_constants import PATH, DATA_TYPE


class GenerateScrollSpeeds:
    """
        generate scroll speeed entries
    """
    __SCROLL_SPEEDS = [
        "FASTEST",
        "FAST",
        "NORMAL",
        "SLOW",
        "SLOWEST"
    ]
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """
            generates table entries
            @return Tuple[ConstantsTableRow, ...]
        """
        table = []
        i = 1
        for speed in GenerateScrollSpeeds.__SCROLL_SPEEDS:
            table_row = ConstantsTableRow(
                name = f'SCROLL_{speed}',
                path = PATH,
                data_type = DATA_TYPE,
                value = i,
                comment = ''
            )
            table.append(table_row)
            i += 1
        return tuple(table)