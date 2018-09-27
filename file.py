import time
import ast

def writeToFile(fileName, content):
    if isinstance(fileName, str) == False:
        fileName = str(fileName)

    f = open(fileName + ".txt","w+")
    f.write(str(content))
    f.close()

def readFile(fileName):
    if isinstance(fileName, str) == False:
        fileName = str(fileName)

    f = open(fileName + ".txt", "r")
    f = f.read()
    return(f)

def fileToArray(fileName):
    if isinstance(fileName, str) == False:
        fileName = str(fileName)

    start_time = time.time()
    file = readFile(fileName)

    array = []
    for i in file:
        if i.isdigit() == True:
            array.append(int(i))
    # array = ast.literal_eval(file)
    # print(array)
    print(time.time()-start_time)
    return array
