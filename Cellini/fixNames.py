import os


os.chdir("json/")
_files = os.listdir()

for _file in _files:
    if _file.startswith("ER"):
        pre = "cellini_ER"
        os.rename(_file, _file.replace("ER", pre))

    elif _file.startswith("ND"):
        pre = "cellini_ND"
        os.rename(_file, _file.replace("ND", pre))

    elif _file.startswith("NE"):
        pre = "cellini_NE"
        os.rename(_file, _file.replace("NE", pre))
