from xlrd import open_workbook

excell_file = "E:/Manoj/Code/My Projects/Python_Practice/temp/sample_excel.xlsx"

wb = open_workbook(excell_file)

for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    for row in range(1, number_of_rows):
        for col in range(number_of_columns):
            print(sheet.cell(row, col).value)
