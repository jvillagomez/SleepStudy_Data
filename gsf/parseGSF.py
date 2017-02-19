import xlrd
import os


_path = "C:\mednick\gsf\GSF_Demographics.xlsx"

workbook = xlrd.open_workbook(_path)
worksheet = workbook.sheet_by_index(0)
_ids = worksheet.col(0)
_sexs = worksheet.col(2)
_ages = worksheet.col(3)
_bmis = worksheet.col(4)


falseBMIs = ["no STOP BANG questionaire", "no weight provided", ""]

demoRecords = []

for i in range(1, len(_ids)):
  demoRecords.append([int(_ids[i].value) , _sexs[i].value, int(_ages[i].value) if _ages[i].value != '' else "N/A", float(_bmis[i].value) if _bmis[i].value not in falseBMIs else "N/A"])
  print(int(_ids[i].value) , _sexs[i].value, int(_ages[i].value) if _ages[i].value != '' else "N/A", float(_bmis[i].value) if _bmis[i].value not in falseBMIs else "N/A")

