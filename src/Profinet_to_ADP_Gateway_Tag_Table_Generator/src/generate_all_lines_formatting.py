""" generates the tags for all lines formatting
"""

from typing import Tuple
from tag_table_row import TagTableRow
from generate_line_formatting import GenerateLineFormatting

class GenerateAllLinesFormatting:
    """ generates the tags for all lines formatting
    """
    @staticmethod
    def generate(initial_offset:int, line_count:int, direction:str)-> Tuple[TagTableRow, ...]:
        """ class execution method
        """
        table = []
        for i in range(line_count):
            generator = GenerateLineFormatting(
                initial_offset= initial_offset, 
                direction= direction
            )
            for row_ in generator.generate(i):
                table.append(row_)
        return tuple(table)
