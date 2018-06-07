from xlrd import open_workbook
from os.path import dirname

excell_file = dirname(__file__) + "/sample_excel.xlsx"

wb = open_workbook(excell_file)

for each_sheet in wb.sheets():
    number_of_rows = each_sheet.nrows
    number_of_columns = each_sheet.ncols

    for each_row in range(1, number_of_rows):
        for each_col in range(number_of_columns):
            print(each_sheet.cell(each_row, each_col).value)
