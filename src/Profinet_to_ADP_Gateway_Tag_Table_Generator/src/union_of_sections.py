"""
    combines outputs of generators into a flat tuple of ConstantsTableRow
"""


from typing import Tuple
from constants_table_row import ConstantsTableRow


class UnionOfSections:
    """
        combines outputs of generators into a flat tuple of ConstantsTableRow
    """
    @staticmethod
    def combine(sections:Tuple[Tuple[ConstantsTableRow, ...]])-> Tuple[ConstantsTableRow, ...]:
        """
            performs combination
            @return Tuple[ConstantsTableRow, ...]
        """
        _table = []
        for section in sections:
            for row_ in section:
                _table.append(row_)
        return tuple(_table)
    