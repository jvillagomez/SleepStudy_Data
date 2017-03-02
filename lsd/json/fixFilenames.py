import os

_dir = "c:\\mednick\\lsd\\json\\nights\\"

os.chdir(_dir)

for _file in os.listdir():
    newName = _file[:3] + "_nights" + _file[3:]
    os.rename(_file, newName)
