""" generates the tags for all lines formatting
"""

from typing import Tuple
from tag_table_row import TagTableRow
from generate_line_formatting import GenerateLineFormatting

class GenerateLinesFormatting:
    """ generates the tags for all lines formatting
    """
    @staticmethod
    def generate()-> Tuple[TagTableRow, ...]:
        """ class execution method
        """
        table = []
        for i in range(5):
            generator = GenerateLineFormatting()
            for row_ in generator.generate(i):
                table.append(row_)
        return tuple(table)
