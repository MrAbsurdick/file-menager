import os, json


########[ GET FILE LIST IN FOLDER ]########
def getFileList(path: str) -> list:
    files = os.listdir(path)
    allFileList = []
    for file in files:
        allFileList.append(file)
    return allFileList


########[ DELETE FOLDERS AND FILES ]########
def deleteFolder(pathToFile) -> None:
    if os.path.exists(pathToFile):

        folders = [d for d in os.listdir(pathToFile) if os.path.isdir(f'{pathToFile}\{d}')]
        files = [f for f in os.listdir(pathToFile) if os.path.isfile(f'{pathToFile}\{f}')]

        if not files == []:
            for file in files:
                os.remove(f'{pathToFile}\{file}')
        if not folders == []:
            for folder in folders:
                deleteFolder(f'{pathToFile}\{folder}')
        os.rmdir(pathToFile)


########[ SAVE JSON FILE ]########
def jsonWriteToFile(data: dict, pathToFile: str, indentLine: int = 4) -> bool:
	try:
		data = json.dumps(data)
		data = json.loads(str(data))
		with open(pathToFile, 'w', encoding = 'utf-8') as file:
			json.dump(data, file, indent = indentLine)
	except:
		return False
	else:
		return True


########[ UPLOADS A JSON FILE TO DICT PYTHON ]########
def jsonToDict(pathToFile: str) -> dict:
	try:
		with open(pathToFile, 'r') as file:
			objectDict = json.loads(file.read())
	except:
		return False
	return objectDict