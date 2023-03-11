"""
    writes to file
"""


from typing import Tuple
import xlsxwriter
from constants_table_row import ConstantsTableRow


class FileWriter:
    """
        writes output excel file
    """
    @staticmethod
    def write(file_name:str, data:Tuple[ConstantsTableRow, ...])-> None:
        """
            writes to file
            @property file_name: str - path and file name to write to
            @property data: str - text to be written to file
            @return None
        """
        work_book = xlsxwriter.Workbook(file_name)
        work_sheet = work_book.add_worksheet(name='Constants')
        row_ = 0
        col_ = 0
        work_sheet.write(row_, col_, 'Name')
        work_sheet.write(row_, col_+1, 'Path')
        work_sheet.write(row_, col_+2, 'Data Type')
        work_sheet.write(row_, col_+3, 'Value')
        work_sheet.write(row_, col_+4, 'Comment')
        row_ += 1
        for datum in data:
            work_sheet.write(row_, col_, datum.name)
            work_sheet.write(row_, col_+1, datum.path)
            work_sheet.write(row_, col_+2, datum.data_type)
            work_sheet.write(row_, col_+3, datum.value)
            work_sheet.write(row_, col_+4, datum.comment)
            row_ += 1
        work_book.close()
        return
