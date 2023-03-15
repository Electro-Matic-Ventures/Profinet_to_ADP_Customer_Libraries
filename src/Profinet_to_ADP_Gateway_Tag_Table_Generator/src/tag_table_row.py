"""
    data class for tag table row
"""


from typing import Tuple


class TagTableRow:
    """ data class for tag table row
    """
    name: str
    path: str
    data_type: str
    logical_address: str
    comment: str
    hmi_visible: str
    hmi_accessible: str
    hmi_writeable: str
    typeobject_id: str
    version_id: str
    def __init__(
        self,
        name:str="",
        path:str="",
        data_type:str="",
        logical_address:str="",
        comment:str="",
        hmi_visible:str="True",
        hmi_accesssible:str="True",
        hmi_writeable:str="True",
        typeobject_id:str="",
        version_id:str=""
    ):
        self.name = name
        self.path = path
        self.data_type = data_type
        self.logical_address = logical_address
        self.comment = comment
        self.hmi_visible = hmi_visible
        self.hmi_accessible = hmi_accesssible
        self.hmi_writeable = hmi_writeable
        self.typeobject_id = typeobject_id
        self.version_id = version_id
        return
    def properties(self)-> Tuple[str, ...]:
        """ allows user to easily iterate over properties
        
            Returns:
                Tuple[str, ...]: tuple of class properties
        """
        return self.__dict__.keys()
    def values(self)-> Tuple[str, ...]:
        """ allows user to easily iterate over values

            Returns:
                Tuple[str, ...]: tuple of values
        """
        return self.__dict__.values()
    