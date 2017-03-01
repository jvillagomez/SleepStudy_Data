import os
import xlrd

def getStages():

  _dir = "C:\\mednick\\lsd\\LSD_Napss\\NapPBO\\"

  allRecords = [] #[ {"subjectID":LSD_422, "stages": 1,2,3,...} ]

  for _file in os.listdir(_dir):
    print(_file)

    currentRecord = {
      "subjectID":"",
      "startDate":"",
      "epochStages":"",
      "epochStartTimes":""
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
    for n in range(1,len(stages)+1):
      timestamp = startTime + (n*30)
      epochTime = timestamp if timestamp < 1440 else timestamp-1440
      epochStartTimes.append(epochTime)

    date = idSheet.cell(9,2).value
    startDate = '.'.join([date[3:5],date[:2],date[6:8]])

    currentRecord["subjectID"] = "LSD_" + idSheet.cell(1,1).value
    currentRecord["startDate"] = startDate
    currentRecord["epochStartTime"] = epochStartTimes
    currentRecord["epochEtages"] = stages

    allRecords.append(currentRecord)

  return allRecords

def main():
  getStages()

if __name__ == "__main__":
  main()


