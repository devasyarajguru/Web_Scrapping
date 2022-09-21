from openpyxl import Workbook

wb = Workbook()

sheet = wb.active

wb.save("demo.xlsx")

data = [
    ("id", "name" ,"roll_no"),
    ("id", "name" ,"roll_no"),
    ("id", "name" ,"roll_no"),
    ("id", "name" ,"roll_no"),
]

for row in data:
    sheet.append(row)   

wb.save("demo.xlsx")