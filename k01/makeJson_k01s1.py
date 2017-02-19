import json
import xlrd
import os


def getDemographics():
  _path = "C:\mednick\k01\K01_Study1_All.xlsx"

  workbook = xlrd.open_workbook(_path)
  worksheet = workbook.sheet_by_index(0)
  _ids = worksheet.col(0)
  _sexs = worksheet.col(6)
  _ages = worksheet.col(5)
  _bmis = worksheet.col(4)

  falseBMIs = ["no STOP BANG questionaire", "no weight provided", ""]
  demoRecords = []

  for i in range(1, len(_ids)):
    currentRecord = {
      "subjectID":"",
      "sex":"",
      "age":"",
      "BMI":""
    }
#     print(currentRecord)

    currentRecord["subjectID"] = int(_ids[i].value)

    if _sexs[i].value in ['F','f']:
      currentRecord["sex"] = int(0)
    elif _sexs[i].value in ['M','m']:
      currentRecord["sex"] = int(1)
    else:
      currentRecord["sex"] = "N/A"

    currentRecord["age"] = int(_ages[i].value) if _ages[i].value != '' else "N/A"
    currentRecord["bmi"] = round(float(_bmis[i].value),2) if _bmis[i].value not in falseBMIs else "N/A"
    demoRecords.append(currentRecord)
  return demoRecords

def getjson():
  demoData = getDemographics()
  _dir = "C:\\mednick\\k01\\json\\"
  jsonDicts = []
  for _file in os.listdir(_dir):
#     print(_file)
    filepath = _dir + _file
#     print(filepath)
    with open(filepath, 'r') as jsonFile:
#       print("opened")
#       print(jsonFile)
      jsonString = jsonFile.read()#.replace('\n', '')
#       print(jsonString)
#       print("read")
      jsonDict = json.loads(jsonString)

    for demo in demoData:
      if int(jsonDict["subjectID"])==int(demo["subjectID"]):
        print(jsonDict["subjectID"], demo["subjectID"])
        jsonDict["age"] = demo["age"]
        jsonDict["BMI"] = demo["bmi"]
        jsonDict["sex"] = demo["sex"]

        print(jsonDict["age"])
      with open(filepath, 'w') as jsonFile:
        jsonString = json.dumps(jsonDict)
        jsonFile.write(jsonString)

  return jsonDicts

def main():
  getjson()



if __name__=="__main__":
  main()
