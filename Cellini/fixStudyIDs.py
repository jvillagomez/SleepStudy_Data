import os

subStudies = ['ER','ND','NE']
newStrings = ['cellini_ER','cellini_ND','cellini_NE']

os.chdir("json/")
_files = os.listdir()

for _file in _files:
    for i in range(3):
        if subStudies[i] in _file:
            oldFile = open(_file,'r')
            content = oldFile.read()
            oldFile.close()
            
            content = content.replace(subStudies[i],newStrings[i])
            newFile = open(_file, 'w+')
            newFile.write(content)


            print(_file)
