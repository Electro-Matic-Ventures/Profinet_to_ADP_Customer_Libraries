"""
    generates constants table for use in TIA Portal
"""


from generate_fonts import GenerateFonts
from generate_scroll_speeds import GenerateScrollSpeeds
from generate_vertical_alignments import GenerateVerticalAlignments
from generate_horizontal_alignments import GenerateHorizontalAlignments
from generate_foreground_colors import GenerateForegroundColors
from generate_background_colors import GenerateBackgroundColors
from generate_flashes import GenerateFlashes
from union_of_sections import UnionOfSections
from file_writer import FileWriter

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
    table.append(generator())
table = UnionOfSections.combine(tuple(table))
FileWriter.write('./output/test.xlsx', table)
