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

jsonSTRINGS = []

for i in range(1, len(_ids)):
  for _file in os.listdir():
    if _file.endswith(".json") and _file.startswith("GSF2015"):

      idtrim1 = _file.replace(_file[:8],'')
      idtrim2 = idtrim1.replace(idtrim1[3:],'')
      
#      print(idtrim2, str(_ids[i].value))

      if int(idtrim2) == int(_ids[i].value):
        print(_file)

        with open(_file,"r") as jsonFile:
          _list = jsonFile.read().split(';')
          stages = _list[0].split(',')
          stages = list(map(int, stages))
          times = _list[1].split(',')
          times = list(map(float, times))

          _id = "gsf_" + str(int(_ids[i].value))
          _sex = _sexs[i].value

          if str(_sex) in ['f','F']:
            _sex = 0
          elif(str(_sex) in ['m','M']):
            _sex = 1


          
          _age = int(_ages[i].value) if _ages[i].value != '' else "N/A"
          _bmi = float(_bmis[i].value) if _bmis[i].value not in falseBMIs else "N/A"


          jsonObj = {
            "epochStartTimes": times, 
            "timeSpentAwake": "N/A", 
            "sessionID": 1, 
            "timeSleptBefore": "N/A", 
            "age": _age, 
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
            "epochStages": stages, 
            "sex": _sex, 
            "bmi": _bmi, 
            "subjectID": _id, 
            "studyID": "GSF_2015"
          }
        
          jsonString = json.dumps(jsonObj)
          #jsonSTRINGS.append(jsonString)


          _filePath = "GSF_2015" + _id + ".json"

          with open(_filePath, 'w') as newfile:
            newfile.write(jsonString)













