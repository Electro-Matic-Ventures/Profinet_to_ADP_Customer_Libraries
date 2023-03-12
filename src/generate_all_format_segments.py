""" generates the tags for all format segments
"""

from typing import Tuple
from tag_table_row import TagTableRow
from generate_format_segment import GenerateFormatSegment

class GenerateAllFormatSegments:
    """ generates the tags for all format segments
    """
    @staticmethod
    def generate(segment_count:int, direction:str)-> Tuple[Tuple[TagTableRow, ...], ...]:
        """ class execution method
        """
        tables = []
        for i in range(segment_count):
            table = []
            generator = GenerateFormatSegment(direction)
            for row_ in generator.generate(i):
                table.append(row_)
            tables.append(tuple(table))
        return tuple(tables)
