import json
import xlrd
import os



def getDemographics():
  _path = "C:\mednick\Cellini\Demographics\Demographic_HS_nights.xlsx"
  falseBMIs = ["no STOP BANG questionaire", "no weight provided", ""," "]

  workbook = xlrd.open_workbook(_path)
  worksheet = workbook.sheet_by_index(0)
  _ids = worksheet.col(0)
  _sexs = worksheet.col(2)
  #_ages = worksheet.col(1)
  _bmis = worksheet.col(5)[1:]

  demoRecords = []

  bmiLim = len(_bmis)-1

  for i in range(1, len(_ids)):
    currentRecord = {
      "studyID":"",
      "subjectID":"",
      "sex":"",
      "BMI":""
    }
    
    currentRecord["studyID"] = (_ids[i].value)[:-2]
    currentRecord["subjectID"] = int((_ids[i].value)[-2:])
    currentRecord["sex"] = int(_sexs[i].value)
    currentRecord["age"] = 'N/A' #int(_ages[i].value) if _ages[i].value not in falseBMIs else "N/A"

    if i > bmiLim:
      currentRecord["BMI"] = "N/A"
    else:
      currentRecord["BMI"] = round(float(_bmis[i].value),2)
    
    demoRecords.append(currentRecord)
    #print(currentRecord)

  return demoRecords

##getDemographics()
#=====================================================================

def getStages():

  _dir = "C:\\mednick\\Cellini\\ScoreFiles\\HS\\"

  allRecords = [] #[ {"subjectID":LSD_422, "stages": 1,2,3,...} ]


  for _file in os.listdir(_dir):
    
    print(_file)
    currentRecord = {
      "studyID":"",
      "subjectID":"",
      "startDate":"",
      "epochStage":"",
      "epochStartTime":[]
    }
    stages = []
    #print(_file)

    excelFile = xlrd.open_workbook(_dir+_file)
    stagesSheet = excelFile.sheet_by_name('GraphData')
    idSheet = excelFile.sheet_by_name('Report')
    
    stagesCol = stagesSheet.col(1)
    del stagesCol[0]
    for stage in stagesCol:
      if int(stage.value) in [-1,0,1,2,3,4,5,6]:
          stages.append(int(stage.value))
    time = idSheet.cell(16,2).value
    #print(time)
    
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
    
    currentRecord["studyID"] = _fileName[:2]
    currentRecord["subjectID"] = _fileName[2:]
    currentRecord["startDate"] = startDate
    currentRecord["epochStartTime"] = epochStartTimes
    currentRecord["epochStage"] = stages
    print(len(stages))
    
    allRecords.append(currentRecord)

  return allRecords

def main():
  demoData = getDemographics()
  stageData = getStages()

  print(demoData[0], stageData[0])

  for stage in stageData:
    for demo in demoData:
      if (int(stage["subjectID"]) == int(demo["subjectID"])) and (stage["studyID"] == demo["studyID"]):
        print(stage["subjectID"], demo["subjectID"], stage["studyID"], demo["studyID"])

        subjectID = demo["subjectID"]
        age = demo["age"]
        sex = demo["sex"]
        bmi = demo["BMI"]
        startDate = stage["startDate"]
        epochStages = stage["epochStage"]
        epochStartTimes = stage["epochStartTime"]
        studyID = "cellini_"+demo['studyID']
        sessionID = 1
        visitID = stage["visitID"]


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
