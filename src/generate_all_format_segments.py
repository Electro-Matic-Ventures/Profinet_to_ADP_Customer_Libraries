""" generates the tags for all format segments
"""

from typing import Tuple
from tag_table_row import TagTableRow
from generate_format_segment import GenerateFormatSegment

class GenerateAllFormatSegments:
    """ generates the tags for all format segments
    """
    @staticmethod
    def generate()-> Tuple[TagTableRow, ...]:
        """ class execution method
        """
        table = []
        format_segment_count = 18
        for i in range(format_segment_count):
            generator = GenerateFormatSegment()
            for row_ in generator.generate(i):
                table.append(row_)
        return tuple(table)
