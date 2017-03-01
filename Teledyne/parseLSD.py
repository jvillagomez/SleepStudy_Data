import xlrd
import os



def getDemographics():
  _path = "C:\mednick\lsd\LSD Demographics.xlsx"

  workbook = xlrd.open_workbook(_path)
  worksheet = workbook.sheet_by_index(0)
  _ids = worksheet.col(0)
  _sexs = worksheet.col(2)
  _ages = worksheet.col(3)
  _bmis = worksheet.col(6)

  falseBMIs = ["no STOP BANG questionaire", "no weight provided", ""]
  demoRecords = []

  for i in range(1, len(_ids)):
    currentRecord = {
      "subjectID":"",
      "sex":"",
      "age":"",
      "bmi":""
    }

    currentRecord["subjectID"] = "LSD_"+str(int(_ids[i].value))

    if _sexs[i].value in ['F','f']:
      currentRecord["sex"] = int(0)
    elif _sexs[i].value in ['M','m']:
      currentRecord["sex"] = int(1)
    else:
      currentRecord["sex"] = "N/A"

    currentRecord["age"] = int(_ages[i].value) if _ages[i].value != '' else "N/A",
    currentRecord["bmi"] = round(float(_bmis[i].value),2) if _bmis[i].value not in falseBMIs else "N/A"
    demoRecords.append(currentRecord)

  return demoRecords




print(getDemographics())
