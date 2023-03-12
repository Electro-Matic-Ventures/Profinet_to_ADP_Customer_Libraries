"""
    generates constants table for use in TIA Portal
"""

from generate_all_constants import GenerateAllConstants
from generate_all_format_segments import GenerateAllFormatSegments
from generate_all_lines_formatting import GenerateAllLinesFormatting
from file_writer import FileWriter

# generate tables
constants_table = GenerateAllConstants.generate()
line_formattting_table = GenerateAllLinesFormatting.generate()
format_segments_tables = GenerateAllFormatSegments.generate()
# write tables to file
file_writer = FileWriter('./output/test.xlsx')
file_writer.write_constants(constants_table)
file_writer.write_constants(line_formattting_table)
for i, segment in enumerate(format_segments_tables):
    file_writer.write_format_segment(i, segment,)
file_writer.close_workbook()
