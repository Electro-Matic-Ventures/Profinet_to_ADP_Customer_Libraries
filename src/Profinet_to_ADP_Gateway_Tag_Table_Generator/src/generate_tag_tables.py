"""
    generates constants table for use in TIA Portal
"""

from generate_all_constants import GenerateAllConstants
from generate_all_format_segments import GenerateAllFormatSegments
from generate_all_lines_formatting import GenerateAllLinesFormatting
from file_writer import FileWriter

# generate tables
constants_table = GenerateAllConstants.generate()
line_formattting_table = GenerateAllLinesFormatting.generate(
    initial_offset= 0,
    line_count= 5,
    direction= "Q"
)
format_segments_tables = GenerateAllFormatSegments.generate(
    initial_offset= 50,
    segment_count= 18,
    direction= "Q"
)
# write tables to file
file_writer = FileWriter('./output/test.xlsx')
file_writer.write_constants(constants_table)
file_writer.write_plc_tags(line_formattting_table)
file_writer.write_plc_tags(format_segments_tables)
file_writer.close_workbook()
