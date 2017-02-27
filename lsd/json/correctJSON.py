import os

_dir = "c:\\mednick\\lsd\\json\\naps\\"

os.chdir(_dir)

for _file in os.listdir():
    print(_file)
    oldID = _file[0:7]
    newID = oldID[-3:]
    print(newID)

    jsonFile = open(_file, 'r')
    jsonString = jsonFile.read()
    jsonFile.close()
    
    jsonString = jsonString.replace(oldID,newID)
    jsonString = jsonString.replace("epochStartTimes","epochStartTime")
    jsonString = jsonString.replace("epochStages","epochStage")
    jsonString = jsonString.replace("epochStages","epochStage")
    jsonString = jsonString.replace("bmi","BMI")
    print(jsonString)
    

    newFile = open(_file, 'w+')
    newFile.write(jsonString)
    newFile.close()
