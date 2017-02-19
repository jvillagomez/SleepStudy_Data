import xlrd
import os

_dir = "C:\\mednick\\lsd\\LSD_Nights\\NapPBO\\"

allRecords = [] #[ {"subjectID":LSD_422, "stages": 1,2,3,...} ]

for _file in os.listdir(_dir):
  print(_file)

  currentRecord = {
    "subjectID":"",
    "stages":""
  }
  stages = []

  excelFile = xlrd.open_workbook(_dir+_file)
  idSheet = excelFile.sheet_by_name('Report')
  stagesSheet = excelFile.sheet_by_name('Stage File')

  stagesCol = stagesSheet.col(1)
  del stagesCol[0]
  for stage in stagesCol:
    stages.append(int(stage.value))

  currentRecord["subjectID"] = idSheet.cell(1,1).value
  currentRecord["stages"] = stages

  allRecords.append(currentRecord)

print(allRecords)
