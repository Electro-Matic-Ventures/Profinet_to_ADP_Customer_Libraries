""" generates all rows for the sole consatnts table
"""

from typing import Tuple
from generate_fonts import GenerateFonts
from generate_scroll_speeds import GenerateScrollSpeeds
from generate_vertical_alignments import GenerateVerticalAlignments
from generate_horizontal_alignments import GenerateHorizontalAlignments
from generate_foreground_colors import GenerateForegroundColors
from generate_background_colors import GenerateBackgroundColors
from generate_flashes import GenerateFlashes
from constants_table_row import ConstantsTableRow

class GenerateAllConstants:
    """ generate all rows of constants table
    
        Methods:
            generate()-> Tuple[ConstantsTableRow, ...]: class execution method
    """
    @staticmethod
    def generate()-> Tuple[ConstantsTableRow, ...]:
        """ generates all rows of constants table

            Returns:
                Tuple[ConstantsTableRow, ...]: all rows of constants table
        """
        generators = [
            GenerateFonts.generate,
            GenerateScrollSpeeds.generate,
            GenerateHorizontalAlignments.generate,
            GenerateVerticalAlignments.generate,
            GenerateForegroundColors.generate,
            GenerateBackgroundColors.generate,
            GenerateFlashes.generate
        ]
        table = []
        for generator in generators:
            for row_ in generator():
                table.append(row_)
        return table
    