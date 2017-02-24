import xlrd
import os
import json


_path = "C:\mednick\gsf\GSF_Demographics.xlsx"

_dir ="C:\\mednick\\gsf\\GSF\\Nap"

workbook = xlrd.open_workbook(_path)
worksheet = workbook.sheet_by_index(0)
_ids = worksheet.col(0)
_sexs = worksheet.col(2)
_ages = worksheet.col(3)
_bmis = worksheet.col(4)


falseBMIs = ["no STOP BANG questionaire", "no weight provided", ""]

demoRecords = []

os.chdir("C:\\mednick\\gsf\\GSF\\Nap")

for i in range(1, len(_ids)):
  for _file in os.listdir():
    if _file.endswith(".json"):

      idtrim1 = _file.replace(_file[:8],'')
      idtrim2 = idtrim1.replace(idtrim1[3:],'')
      
#      print(idtrim2, str(_ids[i].value))

      if int(idtrim2) == int(_ids[i].value):
        print(_file)

        with open(_file,"r") as jsonFile:
          _list = jsonFile.read().split(';')
          stages = _list[0].split(',')
          stages = map(int, stages)
          times = _list[1].split(',')
          times = map(float, times)

          _id = int(_ids[i].value)
          _sexs = _sexs[i].value
          _ages = int(_ages[i].value) if _ages[i].value != '' else "N/A"
          _bmis = float(_bmis[i].value) if _bmis[i].value not in falseBMIs else "N/A"


          jsonObj = {
            "epochStartTimes": [], 
            "timeSpentAwake": "N/A", 
            "sessionID": 1, 
            "timeSleptBefore": "N/A", 
            "age": 19, 
            "visitID": 1, 
            "health": 
            {
              "narcolepsy": "NaN", 
              "depression": "NaN", 
              "sleepApnea": "NaN", 
              "cai": "NaN", 
              "insomnia": "NaN", 
              "rdi": "NaN", 
              "oahi": "NaN", 
              "sleepDisorders": "NaN", 
              "ahi": "NaN", 
              "oai": "NaN"
            }, 
            "startDate": "NaN", 
            "epochStages": [], 
            "sex": 0, 
            "bmi": 22.59, 
            "subjectID": "LSD_422", 
            "studyID": "LSD_Naps"
          }











          

  #print(int(_ids[i].value) , _sexs[i].value, int(_ages[i].value) if _ages[i].value != '' else "N/A", float(_bmis[i].value) if _bmis[i].value not in falseBMIs else "N/A")

