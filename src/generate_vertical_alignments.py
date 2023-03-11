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
        "BOTTOM",
        "MIDDLE",
        "TOP",
        "FILL"
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
                name= f'VERTICAL_{alignment}',
                path= PATH,
                data_type= DATA_TYPE,
                value= i,
                comment= ''
            )
            table.append(table_row)
            i += 1
        return tuple(table)