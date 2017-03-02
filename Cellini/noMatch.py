import os
import json
import xlrd

_list = [    
    "cellini_ND_07",
    "cellini_ND_28",
    "cellini_ND_57",
    "cellini_ND_66"
    ]

def getStages():

  _dir = "C:\\mednick\\Cellini\\ScoreFiles\\ND\\"
  allRecords = [] #[ {"subjectID":LSD_422, "stages": 1,2,3,...} ]

  _noDemos = []

  print(os.listdir(_dir))
  for _file in os.listdir(_dir):
      if _file.replace(".xlsx","") in _list:
          _noDemos.append(_file)
          

  for _file in _noDemos:
    
    print(_file)
    currentRecord = {
      "studyID":"",
      "subjectID":"",
      "startDate":"",
      "epochStage":"",
      "epochStartTime":[]
    }
    stages = []

    excelFile = xlrd.open_workbook(_dir+_file)
    stagesSheet = excelFile.sheet_by_name('GraphData')
    idSheet = excelFile.sheet_by_name('Report')
    
    stagesCol = stagesSheet.col(1)
    del stagesCol[0]
    for stage in stagesCol:
      if int(stage.value) in [-1,0,1,2,3,4,5,6]:
          stages.append(int(stage.value))
    time = idSheet.cell(16,2).value
    
    h, m, s = time.split(':')
    s=(int(s)/60)
    startTime = int(h)*60 + int(m) + round((s * 2) / 2)
    epochStartTimes = []
    epochStartTimes.append(startTime)
    for stage in stages:
      startTime = startTime + 0.5
      if startTime > 1439.5:
        epochStartTimes.append(startTime-1440)
      else:
        epochStartTimes.append(startTime)

    date = idSheet.cell(9,2).value
      
    startDate = '.'.join([date[3:5],date[:2],date[6:8]])

    _fileName = _file.replace(".xlsx","").replace("all","")

    print(_fileName)
    
    currentRecord["studyID"] = _fileName[:11]
    currentRecord["subjectID"] = _fileName[11:] # cellini_ND_1
    currentRecord["startDate"] = startDate
    currentRecord["epochStartTime"] = epochStartTimes
    currentRecord["epochStage"] = stages
    print(len(stages))
    
    allRecords.append(currentRecord)

  return allRecords

def main():
  stageData = getStages()

  for stage in stageData:
    subjectID = stage['subjectID']
    age = "N/A"
    sex = "N/A"
    bmi = "N/A"
    startDate = stage["startDate"]
    epochStages = stage["epochStage"]
    epochStartTimes = stage["epochStartTime"]
    studyID = stage['studyID']
    sessionID = 1
    visitID = 1

    timeSleptBefore = "N/A"
    timeSpentAwake = "N/A"

    jsonDict = {
        "subjectID":subjectID,
        "age":age,
        "BMI":bmi,
        "sex":sex,
        "epochStage":epochStages,
        "epochStartTime":epochStartTimes,
        "startDate":startDate,
        "studyID":studyID,
        "visitID":visitID,
        "sessionID":1,
        "timeSleptBefore":timeSleptBefore,
        "timeSpentAwake":timeSpentAwake,
        "health": {
            "oahi": "NaN",
            "sleepApnea": "NaN",
            "oai": "NaN",
            "insomnia": "NaN",
            "cai": "NaN",
            "ahi": "NaN",
            "depression": "NaN",
            "rdi": "NaN",
            "sleepDisorders": "NaN",
            "narcolepsy": "NaN"}
        }

    filePath = "C:\\mednick\\Cellini\\json\\" + studyID + "_" + str(subjectID) + ".json"

    with open(filePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(jsonDict))
        print(filePath)

if __name__=="__main__":
  main()
