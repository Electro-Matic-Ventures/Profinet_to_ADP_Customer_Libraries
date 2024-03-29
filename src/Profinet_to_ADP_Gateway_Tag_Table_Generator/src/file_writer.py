"""
    writes to file
"""


from typing import Tuple
import xlsxwriter
from constants_table_row import ConstantsTableRow
from tag_table_row import TagTableRow


class FileWriter:
    """ writes output excel file
    """
    __work_book: xlsxwriter.Workbook
    __row: int
    __PLC:str = 'PLC Tags'
    __CONSTANTS: str = 'Constants'
    def __init__(self, file_name:str):
        self.__work_book = xlsxwriter.Workbook(file_name)
        self.__create_constants_worksheet()
        self.__create_plc_tags_worksheet()
        return
    def __create_constants_worksheet(self)-> None:
        work_sheet = self.__work_book.add_worksheet(self.__CONSTANTS)
        column_labels = [
            "Name",
            "Path",
            "Data Type",
            "Value",
            "Comment"
        ]
        for i, label in enumerate(column_labels):
            work_sheet.write(0, i, label)
        return
    
    def __create_plc_tags_worksheet(self)-> None:
        work_sheet = self.__work_book.add_worksheet(self.__PLC)
        column_labels = [
            "Name",
            "Path",
            "Data Type",
            "Logical Address",
            "Comment",
            "HMI Visible",
            "HMI Accessible",
            "HMI Writeable",
            "Typeobject ID",
            "Version ID"
        ]
        for i, label in enumerate(column_labels):
            work_sheet.write(0, i, label)
        self.__row = 1
        return
    
    def write_constants(self, data:Tuple[ConstantsTableRow, ...])-> None:
        """ write constants section
            @property data (Tuple[ConstantsTableRow, ...]): data for the Constants table
            @return (None): writes to class property __work_book
        """
        work_sheet = self.__work_book.get_worksheet_by_name(self.__CONSTANTS)
        row_ = 1
        for datum in data:
            work_sheet.write(row_, 0, datum.name)
            work_sheet.write(row_, 1, datum.path)
            work_sheet.write(row_, 2, datum.data_type)
            work_sheet.write(row_, 3, datum.value)
            work_sheet.write(row_, 4, datum.comment)
            row_ += 1
        return\
            
    def write_plc_tags(self, data:Tuple[TagTableRow, ...])-> None:
        """ write line formats section
        
            Args:
                data (Tuple[TagTableRow, ...]): data for the line formats section of 
                the PLC Tags table
            
            Returns:
                int: next available row index in PLC Tags worksheet
        """
        work_sheet = self.__work_book.get_worksheet_by_name(self.__PLC)
        for datum in data:
            work_sheet.write(self.__row, 0, datum.name)
            work_sheet.write(self.__row, 1, datum.path)
            work_sheet.write(self.__row, 2, datum.data_type)
            work_sheet.write(self.__row, 3, datum.logical_address)
            work_sheet.write(self.__row, 4, datum.comment)
            work_sheet.write(self.__row, 5, datum.hmi_visible)
            work_sheet.write(self.__row, 6, datum.hmi_accessible)
            work_sheet.write(self.__row, 7, datum.hmi_writeable)
            work_sheet.write(self.__row, 8, datum.typeobject_id)
            work_sheet.write(self.__row, 9, datum.version_id)
            self.__row += 1
        return
    def close_workbook(self)-> None:
        """ closes workbook            
        """
        self.__work_book.close()
        return
    