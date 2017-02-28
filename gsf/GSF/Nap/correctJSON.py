import os

_dir = "C:\\mednick\\gsf\\GSF\\Nap\\json\\"

os.chdir(_dir)

for _file in os.listdir():
    print(_file)
    _name = _file.replace(".json","")
    newID = _name[-3:]
    oldID = "gsf_" + newID

    jsonFile = open(_file, 'r')
    jsonString = jsonFile.read()
    jsonFile.close()
    
    jsonString = jsonString.replace(oldID,newID)
    #jsonString = jsonString.replace("epochStartTimes","epochStartTime")
    #jsonString = jsonString.replace("epochStages","epochStage")
    #jsonString = jsonString.replace("epochStages","epochStage")
    #jsonString = jsonString.replace("bmi","BMI")
    print(jsonString)
    

    newFile = open(_file, 'w+')
    newFile.write(jsonString)
    newFile.close()
