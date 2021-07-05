import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet.cell(1, 1)
print(cell.value)
#Error 13... permision... subject for consultation with Nats