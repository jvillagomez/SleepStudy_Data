import json
import scipy.io
import os


_dir = "C:\\mednick\\gsf\\GSF\\Nap\\"

os.chdir(_dir)
files = []

for _file in os.listdir(_dir):
    if _file.endswith('.mat'):
        files.append(_file)

for _file in files:
    prefile = _file.replace(_file[:8],'')
    _id = prefile.replace(prefile[3:],'')
    
    matObj = scipy.io.loadmat(_file)
    matData = matObj['stageData']

    stages = matData[0][0][5]
    times = matData[0][0][7]

    epochStages = []
    epochTimes = []
    for i in range(0,len(stages)):
        epochStages.append(str(stages[i][0]))
        epochTimes.append(str(times[0][i]))

    stagesStr = ','.join(epochStages)
    timesStr = ','.join(epochTimes)
    _array = ';'.join([stagesStr, timesStr])

    for l in range(0,len(epochStages)):
        epochStages[l] = int(epochStages[l])
    for l in range(0,len(epochStages)):
        epochTimes[l] = round(float(epochTimes[l]), 1)

    jsonDict = {"subjectID":int(_id),
                "epochTimes":epochTimes,
                "epochStages":epochStages
                }

    jsonString = json.dumps(jsonDict)

    print(jsonDict)
    print(jsonString)

    newPath = _file.replace(".mat",".json")
    with open(newPath, 'w') as newFile:
        newFile.write(_array)
