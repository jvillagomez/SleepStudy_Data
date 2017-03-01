import json
import xlrd
import os


def getDemographics():
  _path = "C:\\mednick\\Teledyne\\Demographics\\Demographics _TD_naps.xlsx"
  falseBMIs = ["no STOP BANG questionaire", "no weight provided", ""," "]

  workbook = xlrd.open_workbook(_path)
  worksheet = workbook.sheet_by_index(0)
  _ids = worksheet.col(0)
  _sexs = worksheet.col(2)
  _ages = worksheet.col(3)
  _bmis = worksheet.col(6)

  demoRecords = []

  for i in range(1, len(_ids)):
    currentRecord = {
      "subjectID":"",
      "sex":"",
      "BMI":""
    }

    currentRecord["subjectID"] = "LSD_"+str(int(_ids[i].value))
    currentRecord["sex"] = int(_sexs[i].value)
    currentRecord["age"] = int(_ages[i].value) if _ages[i].value not in falseBMIs else "N/A"
    currentRecord["BMI"] = round(float(_bmis[i].value),2) if _bmis[i].value not in falseBMIs else "N/A"

    demoRecords.append(currentRecord)

  return demoRecords

def getStages():

  _dir = "C:\\mednick\\Teledyne\\ScoreFiles\\"

  allRecords = [] #[ {"subjectID":LSD_422, "stages": 1,2,3,...} ]

  for _file in os.listdir(_dir):
    currentRecord = {
      "subjectID":"",
      "startDate":"",
      "epochStage":"",
      "epochStartTime":[]
    }
    stages = []

    excelFile = xlrd.open_workbook(_dir+_file)
    idSheet = excelFile.sheet_by_name('Report')
    stagesSheet = excelFile.sheet_by_name('Stage File')

    stagesCol = stagesSheet.col(1)
    del stagesCol[0]
    for stage in stagesCol:
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

    currentRecord["subjectID"] = idSheet.cell(1,1).value
    currentRecord["startDate"] = startDate
    currentRecord["epochStartTime"] = epochStartTimes
    currentRecord["epochStage"] = stages
    currentRecord["filename"] = _file

    if any(word in _file for word in ["v1", "V1"]):

      currentRecord["visitID"] = 1
    elif (any(word in _file for word in ["v2", "V2"])):
      currentRecord["visitID"] = 2
    elif (any(word in _file for word in ["v3", "V3"])):
      currentRecord["visitID"] = 3
    elif (any(word in _file for word in ["v4", "V4"])):
      currentRecord["visitID"] = 4
    elif (any(word in _file for word in ["v5", "V5"])):
      currentRecord["visitID"] = 5
    else:
      currentRecord["visitID"] = 1

    print(currentRecord["subjectID"],currentRecord["visitID"])

    allRecords.append(currentRecord)

  return allRecords



def main():
  demoData = getDemographics()
  print(len(demoData))
  stageData = getStages()
  print(len(stageData))

  stageIDs = []
  demoIDs = []

  for stage in stageData:
    stageIDs.append(stage["subjectID"])
  for demo in demoData:
    demoIDs.append(demo["subjectID"])


  for stage in stageData:
    if stage['subjectID'] in demoIDs:
      for demo in demoData:
        verd = (stage["subjectID"] != demo["subjectID"])
        last = (demo["subjectID"]==demoData[-1]["subjectID"])

        if stage["subjectID"] == demo["subjectID"]:
          print(stage["subjectID"], demo["subjectID"])
          subjectID = demo["subjectID"]
          age = demo["age"]
          sex = demo["sex"]
          bmi = demo["bmi"]
          startDate = stage["startDate"]
          epochStages = stage["epochStages"]
          epochStartTimes = stage["epochStartTimes"]
          studyID = "N/A" #data["studyID"]
          sessionID = "N/A" #data["sessionID"]
          visitID = stage["visitID"]
          timeSleptBefore = "N/A" #data["timeSleptBefore"]
          timeSpentAwake = "N/A" #data["timeSpentAwake"]
          jsonDict = {
            "subjectID":subjectID,
            "age":age,
            "bmi":bmi,
            "sex":sex,
            "epochStages":epochStages,
            "epochStartTimes":epochStartTimes,
            "startDate":startDate,
            "studyID":"LSD_Naps",
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

          filePath = "C:\\mednick\\lsd\\json\\naps\\"+subjectID+"_v"+str(visitID)+".json"

          with open(filePath, 'w') as jsonFile:
            jsonFile.write(json.dumps(jsonDict))
            print(filePath)
    else:
      print(stage["subjectID"], demo["subjectID"])
      subjectID = stage["subjectID"]
      startDate = stage["startDate"]
      epochStages = stage["epochStages"]
      epochStartTimes = stage["epochStartTimes"]
      visitID = stage["visitID"]
      jsonDict = {
        "subjectID":subjectID,
        "age": "NaN",
        "bmi": "NaN",
        "sex": "NaN",
        "epochStages":epochStages,
        "epochStartTimes":epochStartTimes,
        "startDate":startDate,
        "studyID":"LSD_Naps",
        "visitID":visitID,
        "sessionID":1,
        "timeSleptBefore": "NaN",
        "timeSpentAwake": "NaN",
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

      filePath = "C:\\mednick\\lsd\\json\\naps\\"+subjectID+"_v"+str(visitID)+".json"

      with open(filePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(jsonDict))
        print(filePath)




if __name__=="__main__":
  main()
