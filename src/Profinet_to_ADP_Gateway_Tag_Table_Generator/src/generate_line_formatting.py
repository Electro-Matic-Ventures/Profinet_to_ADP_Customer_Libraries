""" generates the tags for a single led row of line formatting
"""

from typing import Tuple
from tag_table_row import TagTableRow


class GenerateLineFormatting:
    
    """ generates the ta
    """
    
    __PATH = "Line Formatting"
    __DATA_TYPE = "SInt"
    __DIRECTION: str
    __INITIAL_OFFSET: int
    __line_offset: int
    
    def __init__(self, direction:str="I", initial_offset:int=0):
        self.__DIRECTION = direction
        self.__INITIAL_OFFSET = initial_offset
        self.__line_offset = 0
    
    def generate(self, line_number:int=0)-> Tuple[TagTableRow, ...]:
        """ led sign line formatting rows for the tag table

            Args:
                line_number (int): led sign line number

            Returns:
                Tuple[TagTableRow, ...]: rows to be appended to tag table
        """
        table = []
        self.__line_offset = line_number * 2
        table.append(self.__generate_font_row(line_number))
        table.append(self.__generate_horizontal_alignment_row(line_number))
        return tuple(table)
    
    def __generate_font_row(self, line_number:int)-> TagTableRow:
        name = f'Line_{line_number}_Font_Size_&_Weight'
        return self.__generate_row(name=name, offset=0)
    
    def __generate_horizontal_alignment_row(self, line_number:int)-> TagTableRow:
        name = f'Line_{line_number}_Horizontal_Alignment'
        return self.__generate_row(name=name, offset=1)
    
    def __generate_row(self, name:str, offset:int)-> TagTableRow:
        total_offset = self.__INITIAL_OFFSET + self.__line_offset + offset
        return TagTableRow(
            name= name,
            path= self.__PATH,
            data_type= self.__DATA_TYPE,
            logical_address= f'%{self.__DIRECTION}B{total_offset}'
        )
        