import time
import file

def count(fileName):
    global array
    global countArray
    array = file.fileToArray(fileName)
    countArray = [0] * 10
    for i in array:
        countArray[i] = countArray[i] + 1

    # print(array)
    print(countArray)

def pro():
    global proArray
    proArray = [0] * 10
    summ = sum(countArray)
    for i in range(10):
        proArray[i] = (countArray[i] / summ) * 100
    print(proArray)

def pattern():
    global p
    p = []
    f = 0
    b = False
    arrayLen = len(array)
    for i in range(arrayLen):
        if i != (arrayLen - 1):
            if array[i] == array[i + 1]:
                b = True
                f = f + 1
            elif array[i] != array[i + 1] and b == True:
                nummm = array[i]
                p.append(str(nummm) * (f + 1))
                ##
                ## THIS IS A STING BECAUSE IF YOU CHANGE IT TO AND INT
                ## THE ZEROES WILL ONLY BE ONE ZERO
                ##
                b = False
                f = 0
            else:
                b = False
                f = 0
    # print()
    # print(p)

def pCompresed():
    rr = {}
    for i in set(p):
        rr[i] = 0
    # print(rr)
    for x in p:
        rr[x] = rr[x] + 1
    print(rr)
    # for x in p:
    #     if x ==
    #     print(x)
    # for i in p:
    #     print(set(p))
    #     if set(p) == False:
    #         print(False)
    # print(p)
        # print(rr.index(i))
    # print(p.index('55'))
    # lds = len(p)
    # for i in range(lds):
    #     print(i)

def all(fileName):
    count(fileName)
    pro()
    pattern()
    pCompresed()
