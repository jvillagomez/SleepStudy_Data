import xlrd
import os


_path = "C:\mednick\k01\K01_Study1_All.xlsx"

workbook = xlrd.open_workbook(_path)
worksheet = workbook.sheet_by_index(0)
_ids = worksheet.col(0)
_sexs = worksheet.col(6)
_ages = worksheet.col(5)
_bmis = worksheet.col(4)


falseEntries = ["no STOP BANG questionaire", "no weight provided", "", " "]

demoRecords = []

for i in range(1, len(_ids)):

  demoRecords.append([
      int(_ids[i].value),
      _sexs[i].value if _sexs[i].value not in falseEntries else "N/A",
      int(_ages[i].value) if _ages[i].value not in falseEntries else "N/A",
      float(_bmis[i].value) if _bmis[i].value not in falseEntries else "N/A"
    ])

  print(
    int(_ids[i].value),
    _sexs[i].value if _sexs[i].value not in falseEntries else "N/A",
    int(_ages[i].value)
    if _ages[i].value != '' else "N/A",
    float(_bmis[i].value) if _bmis[i].value not in falseEntries else "N/A"
  )




