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

    
#    newPath = _file.replace(".mat",".csv")
#    with open(newPath, 'w') as newFile:
#        newFile.write(_array)
