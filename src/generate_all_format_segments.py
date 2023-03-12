""" generates the tags for all format segments
"""

from typing import Tuple
from tag_table_row import TagTableRow
from generate_format_segment import GenerateFormatSegment

class GenerateAllFormatSegments:
    """ generates the tags for all format segments
    """
    @staticmethod
    def generate(initial_offset:int, segment_count:int, direction:str)-> Tuple[TagTableRow, ...]:
        """ class execution method
        """
        table = []
        for i in range(segment_count):
            generator = GenerateFormatSegment(
                initial_offset= initial_offset, 
                direction= direction
            )
            for row_ in generator.generate(i):
                table.append(row_)
        return tuple(table)
