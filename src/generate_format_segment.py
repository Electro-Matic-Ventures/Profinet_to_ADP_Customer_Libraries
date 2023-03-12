""" generates the tags for a format segment
"""

from typing import Tuple
from tag_table_row import TagTableRow


class GenerateFormatSegment:
    """ generates the ta
    """
    __PATH = "Format Segment"
    __DATA_TYPE = "Byte"
    __direction: str
    def __init__(self, direction:str="I"):
        self.__direction = direction
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
        for row_ in self.__generate_text(format_segment):
            table.append(row_)
        return tuple(table)
    __INTITAL_OFFSET = 50
    __BYTES_PER_SEGMENT = 50

    def __generate_foreground_color(self, format_segment:int)-> TagTableRow:
        name = f'Format_Segment_{format_segment}_Font_Size_&_Weight'
        offset = self.__INTITAL_OFFSET + format_segment * self.__BYTES_PER_SEGMENT
        return self.__generate_row(name, format_segment, offset)
    def __generate_background_color(self, format_segment:int)-> TagTableRow:
        name = f'Format_Segment_{format_segment}_Scroll_Speed'
        offset = self.__INTITAL_OFFSET + format_segment * self.__BYTES_PER_SEGMENT + 1
        return self.__generate_row(name, format_segment, offset)
    def __generate_flash(self, format_segment:int)-> TagTableRow:
        name = f'Format_Segment_{format_segment}_Vertical_Alignment'
        offset = self.__INTITAL_OFFSET + format_segment * self.__BYTES_PER_SEGMENT + 2
        return self.__generate_row(name, format_segment, offset)
    def __generate_line_number(self, format_segment:int)-> TagTableRow:
        name = f'Format_Segment_{format_segment}_Horizontal_Alignment'
        offset = self.__INTITAL_OFFSET + format_segment * self.__BYTES_PER_SEGMENT + 3
        return self.__generate_row(name, format_segment, offset)
    def __generate_text(self, format_segment:int)-> Tuple[TagTableRow, ...]:
        bytes_ = []
        text_bytes = 50 - 4
        for i in range(text_bytes):
            bytes_.append(self.__generate_text_byte(format_segment, i))
        return tuple(bytes_)
    def __generate_text_byte(self, format_segment:int, index:int)-> TagTableRow:
        name = f'Format_Segment_{format_segment}_Text_Byte_{index}'
        offset = self.__INTITAL_OFFSET + format_segment * self.__BYTES_PER_SEGMENT + 4 + index
        return self.__generate_row(name, format_segment, offset)
    def __generate_row(self, name:str, format_segment:int, offset:int)-> TagTableRow:
        return TagTableRow(
            name=name,
            path=f'{self.__PATH} {format_segment}',
            data_type=self.__DATA_TYPE,
            logical_address=f'%{self.__direction}B{offset}'
        )
        