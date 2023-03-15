"""
    generates vertical alignment sections
"""


from typing import Tuple
from constants_table_row import ConstantsTableRow
from project_constants import PATH, DATA_TYPE


class GenerateVerticalAlignments:
    """
        generates vertical alignment section of table
    """
    __ALIGNMENTS = [
        "middle_hold",
        "fill_hold",
        "bottom_hold",
        "top_hold",
        "bottom_scroll",
        "fill_scroll",
        "middle_scroll",
        "top_scroll"
    ]
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """
            generate table entries
        """
        table = []
        i = 1
        for alignment in GenerateVerticalAlignments.__ALIGNMENTS:
            table_row = ConstantsTableRow(
                name= f'VERTICAL_{alignment.upper()}',
                path= PATH,
                data_type= DATA_TYPE,
                value= i,
                comment= ''
            )
            table.append(table_row)
            i += 1
        return tuple(table)