""" generates the tags for a single led row of line formatting
"""

from typing import Tuple
from tag_table_row import TagTableRow


class GenerateLineFormatting:
    """ generates the ta
    """
    __PATH = "Line Formatting"
    __DATA_TYPE = "Byte"
    def generate(self, line_number:int)-> Tuple[TagTableRow, ...]:
        """ led sign line formatting rows for the tag table

            Args:
                line_number (int): led sign line number

            Returns:
                Tuple[TagTableRow, ...]: rows to be appended to tag table
        """
        table = []
        table.append(self.__generate_font_row(line_number))
        table.append(self.__generate_scroll_speed_row(line_number))
        table.append(self.__generate_vertical_alignment_row(line_number))
        table.append(self.__generate_horizontal_alignment_row(line_number))
        table.append(self.__generate_hold_row(line_number))
        return tuple(table)
    def __generate_font_row(self, line_number:int)-> TagTableRow:
        name = f'Line_{line_number}_Font_Size_&_Weight'
        offset = line_number * 5
        return self.__generate_row(name, offset)
    def __generate_scroll_speed_row(self, line_number:int)-> TagTableRow:
        name = f'Line_{line_number}_Scroll_Speed'
        offset = line_number * 5 + 1
        return self.__generate_row(name, offset)
    def __generate_vertical_alignment_row(self, line_number:int)-> TagTableRow:
        name = f'Line_{line_number}_Vertical_Alignment'
        offset = line_number * 5 + 2
        return self.__generate_row(name, offset)
    def __generate_horizontal_alignment_row(self, line_number:int)-> TagTableRow:
        name = f'Line_{line_number}_Horizontal_Alignment'
        offset = line_number * 5 + 3
        return self.__generate_row(name, offset)
    def __generate_hold_row(self, line_number:int)-> TagTableRow:
        name = f'Line_{line_number}_Hold'
        offset = line_number * 5 + 4
        return self.__generate_row(name, offset)
    def __generate_row(self, name:str, offset:int)-> TagTableRow:
        return TagTableRow(
            name=name,
            path=self.__PATH,
            data_type=self.__DATA_TYPE,
            logical_address=f'$IB{offset}'
        )
        