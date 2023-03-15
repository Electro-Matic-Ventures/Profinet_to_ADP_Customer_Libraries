"""
    data class representing a row of the constants table
"""


from typing import Tuple


class ConstantsTableRow:
    """
        data class representing a rwo of the constants table
        @property name: str 
        @property path: str
        @property data_type: str
        @property value: str
        @property comment: str
    """
    name: str
    path: str
    data_type: str
    value: int
    comment: str
    def __init__(
        self,
        name:str="",
        path:str="",
        data_type:str="",
        value:int=0,
        comment:str=""
    ):
        """
        """
        self.name = name
        self.path = path
        self.data_type = data_type
        self.value = value
        self.comment = comment
        return
    def properties(self)-> Tuple[str, ...]:
        """
            allows user to easily iterate over properties
        """
        return self.__dict__.keys()
    def values(self)-> Tuple[str, ...]:
        """
            allows user to easily iterate over values
        """
        return self.__dict__.values()
