""" generates the tags for a format segment
"""

from typing import Tuple
from tag_table_row import TagTableRow


class GenerateFormatSegment:
    """ generates the ta
    """
    __PATH = "Format Segment"
    __DATA_TYPE = "Byte"
    def generate(self, format_segment:int)-> Tuple[TagTableRow, ...]:
        """ format segment tags for tag table

            Args:
                format_segment (int): format segment number

            Returns:
                Tuple[TagTableRow, ...]: rows to be appended to tag table
        """
        table = []
        table.append(self.__generate_foreground_color(format_segment))
        table.append(self.__generate_background_color(format_segment))
        table.append(self.__generate_flash(format_segment))
        table.append(self.__generate_line_number(format_segment))
        table.append(self.__generate_text(format_segment))
        return tuple(table)
    __OFFSET_BYTES = 50
    def __generate_foreground_color(self, format_segment:int)-> TagTableRow:
        name = f'Format_Segment_{format_segment}_Font_Size_&_Weight'
        offset = format_segment * 50
        return self.__generate_row(name, format_segment, offset)
    def __generate_background_color(self, format_segment:int)-> TagTableRow:
        name = f'Line_{format_segment}_Scroll_Speed'
        offset = format_segment * self.__OFFSET_BYTES + 1
        return self.__generate_row(name, format_segment, offset)
    def __generate_flash(self, format_segment:int)-> TagTableRow:
        name = f'Line_{format_segment}_Vertical_Alignment'
        offset = format_segment * self.__OFFSET_BYTES + 2
        return self.__generate_row(name, format_segment, offset)
    def __generate_line_number(self, format_segment:int)-> TagTableRow:
        name = f'Line_{format_segment}_Horizontal_Alignment'
        offset = format_segment * self.__OFFSET_BYTES + 3
        return self.__generate_row(name, format_segment, offset)
    def __generate_text(self, format_segment:int)-> TagTableRow:
        name = f'Line_{format_segment}_Hold'
        offset = format_segment * self.__OFFSET_BYTES + 4
        return self.__generate_row(name, format_segment, offset)
    def __generate_row(self, name:str, format_segment:int, offset:int)-> TagTableRow:
        return TagTableRow(
            name=name,
            path=f'{self.__PATH}_{format_segment}',
            data_type=self.__DATA_TYPE,
            logical_address=f'$QB{offset}'
        )
        