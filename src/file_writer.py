"""
    writes to file
"""


from typing import Tuple
import xlsxwriter
from constants_table_row import ConstantsTableRow
from tag_table_row import TagTableRow


class FileWriter:
    """
        writes output excel file
    """
    
    def write(file_name:str, data:Tuple[ConstantsTableRow, ...])-> None:
        """
            writes to file
            @property file_name: str - path and file name to write to
            @property data: str - text to be written to file
            @return None
        """
        work_book = xlsxwriter.Workbook(file_name)
        constants_sheet = work_book.add_worksheet(name='Constants')
        tags_sheet = work_book.add_worksheet(name='PLC Tags')
        row_ = 0
        col_ = 0
        for datum in data:
            row_ += 1
            if type(datum) == "ConstantsTableRow":
                FileWriter.__constants(datum)
                continue
            if type(datum) == "TagTableRow":
                FileWriter.__tags(datum)
                continue
        row_ += 1
        work_book.close()
        return
        def __make_constants_sheet()->None:
            work_sheet.write(row_, col_, 'Name')
            work_sheet.write(row_, col_+1, 'Path')
            work_sheet.write(row_, col_+2, 'Data Type')
            work_sheet.write(row_, col_+3, 'Value')
            work_sheet.write(row_, col_+4, 'Comment')
            return
        def __constants(row_:int, datum:ConstantsTableRow)-> None:
            work_sheet.write(row_, 0, datum.name)
            work_sheet.write(row_, 1, datum.path)
            work_sheet.write(row_, 2, datum.data_type)
            work_sheet.write(row_, 3, datum.value)
            work_sheet.write(row_, 4, datum.comment)
            return
        def __tags(row_:int, datum:TagTableRow)-> None:
            if datum.path == "Line Formatting":
                FileWriter.__line_formatting()
                return
            FileWriter.__format_segment()
            return
        def __line_formatting()-> None:
            
            return
        def __format_segment()-> None:
            return