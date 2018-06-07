from os.path import dirname

import xlrd
import xlwt

input_file = dirname(__file__) + "/../sample_excel.xlsx"
output_file = dirname(__file__) + "/output_excel.xls"

input_workbook = xlrd.open_workbook(input_file)
output_workbook = xlwt.Workbook()
output_sheet = output_workbook.add_sheet('test')

for each_sheet in input_workbook.sheets():
    number_of_rows = each_sheet.nrows
    number_of_columns = each_sheet.ncols

    for each_row in range(number_of_rows):
        for each_col in range(number_of_columns):
            cell_content = each_sheet.cell(each_row, each_col).value

            output_sheet.write(each_row, each_col, cell_content)

output_workbook.save(output_file)
