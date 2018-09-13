import xlrd

input_file = "../sample_excel.xlsx"
input_workbook = xlrd.open_workbook(input_file)


for each_sheet in input_workbook.sheets():
    number_of_rows = each_sheet.nrows
    number_of_columns = each_sheet.ncols

    for each_row in range(1, number_of_rows):
        for each_col in range(number_of_columns):
            print(each_sheet.cell(each_row, each_col).value)
