import time
import random
import math

import file
import bar

def randomArray(fileName, numOfRan):
    startTime = time.time()
    ranNum = []

    for i in range(numOfRan):
        ranNum.append(random.randrange(0, 10))
        if (i + 1) % 100 == 0:
            bar.progress(i, numOfRan)

    file.writeToFile(fileName, ranNum)
    howLong = time.time()-startTime
    print("It took", round(howLong, 2), "seconds to generate", numOfRan, "random numbers and write it to", fileName + ".txt")
