"""
    generates horizontal alignment rows for table
"""


from typing import Tuple
from project_constants import PATH, DATA_TYPE
from constants_table_row import ConstantsTableRow


class GenerateHorizontalAlignments:
    """
        generates horizontal alignment rows for table
    """
    __ALIGNMENTS = [
        "LEFT",
        "RIGHT",
        "CENTER"
    ]
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """
            performs operation
        """
        table = []
        i = 1
        for alignment in GenerateHorizontalAlignments.__ALIGNMENTS:
            table_row = ConstantsTableRow(
                name= f'HORIZONTAL_{alignment}',
                path= PATH,
                data_type= DATA_TYPE,
                value= i,
                comment= ''
            )
            table.append(table_row)
            i += 1
        return tuple(table)