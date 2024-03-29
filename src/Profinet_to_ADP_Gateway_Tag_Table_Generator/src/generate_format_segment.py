""" generates the tags for a format segment
"""

from typing import Tuple
from tag_table_row import TagTableRow


class GenerateFormatSegment:
    
    """ generates the ta
    """
    
    __PATH = "Format Segment"
    __DIRECTION: str
    __INITIAL_OFFSET: int
    __row_offset: int
    
    def __init__(self, initial_offset:int=50, direction:str="I"):
        self.__INITIAL_OFFSET = initial_offset
        self.__DIRECTION = direction
        self.__row_offset = 0
        return
    
    def generate(self, format_segment:int)-> Tuple[TagTableRow, ...]:
        """ format segment tags for tag table

            Args:
                format_segment (int): format segment number

            Returns:
                Tuple[TagTableRow, ...]: rows to be appended to tag table
        """
        table = []
        self.__row_offset = 50 * format_segment
        table.append(self.__generate_foreground_color(format_segment))
        table.append(self.__generate_background_color(format_segment))
        table.append(self.__generate_flash(format_segment))
        table.append(self.__generate_line_number(format_segment))
        for row_ in self.__generate_text(format_segment):
            table.append(row_)
        return tuple(table)
    
    def __generate_foreground_color(self, format_segment:int)-> TagTableRow:
        name = f'Segment_Format_{format_segment}_FG_Color'
        row_ = self.__generate_row(
            name= name,
            format_segment= format_segment,
            offset= 0
        )
        return row_
    
    def __generate_background_color(self, format_segment:int)-> TagTableRow:
        name = f'Segment_Format_{format_segment}_BG_Color'
        row_ = self.__generate_row(
            name= name,
            format_segment= format_segment,
            offset= 1
        )
        return row_
    
    def __generate_flash(self, format_segment:int)-> TagTableRow:
        name = f'Segment_Format_{format_segment}_Flash'
        row_ = self.__generate_row(
            name= name,
            format_segment= format_segment,
            offset= 2
        )
        return row_
    
    def __generate_line_number(self, format_segment:int)-> TagTableRow:
        name = f'Segment_Format_{format_segment}_Line_Number'
        row_ = self.__generate_row(
            name= name,
            format_segment= format_segment,
            offset= 3
        )
        return row_
    
    def __generate_text(self, format_segment:int)-> Tuple[TagTableRow, ...]:
        bytes_ = []
        text_bytes = 50 - 4
        for i in range(text_bytes):
            bytes_.append(self.__generate_text_byte(format_segment, i))
        return tuple(bytes_)
    
    def __generate_text_byte(self, format_segment:int, index:int)-> TagTableRow:
        name = f'Segment_Format_{format_segment}_Text_Byte_{index}'
        row_ = self.__generate_row(
            name= name,
            format_segment= format_segment,
            offset= 4 + index,
            data_type= "Char"
        )
        return row_
    
    def __generate_row(self, name:str, format_segment:int, offset:int, data_type:str="SInt")-> TagTableRow:
        total_offset = self.__INITIAL_OFFSET + self.__row_offset + offset
        return TagTableRow(
            name= name,
            path= f'{self.__PATH} {format_segment}',
            data_type= data_type,
            logical_address= f'%{self.__DIRECTION}B{total_offset}'
        )
        