import random
import time
import os
import math
import sys
import ast

ranNum = []
count = [0,0,0,0,0,0,0,0,0,0]
#count = [1,1,1,1,1,1,1,1,1,1]
loop = 10

rows, columns = os.popen('stty size', 'r').read().split()

# def init():
#

def writeToFile(fileName, content):
    f = open(fileName + ".txt","w+")
    f.write(str(content))
    f.close()

def readFile(fileName):
    f = open(fileName + ".txt", "r")
    f = f.read()
    return(f)

def randomLibary():
    for i in range(loop):
        ranNum.append(random.randrange(0, 10))
    # writeToFile("test", ranNum)
    # print(ranNum)
    # print(readFile("test"))

def countList():
    for i in ranNum:
        count[i] = count[i] + 1

def analyse():
    # count how many times every number accours
    countList()


randomLibary()
analyse()

# f = open("ran.txt","w+")
#
# def ran():
#     start_time = time.time()
#     for i in range(loop):
#         ranNum.append(random.randrange(0, 10))
#         if i % 100 == 0:
#             #status = str(i) + "/" + str(loop)
#             print(str(math.floor((i/loop)*100)) + "%", end="\r\r")
#     print("My program took", time.time() - start_time, "to run")
#     f.write(str(ranNum))
#
# ran()

# f = open("ran.txt", "r")
# f = f.read()
# # f = ast.literal_eval(f)
# print(f)
# for i in f:
#     print(i)

# print(ranNum)

#
#
# def makeCount():
#     for i in ranNum:
#         count[i] = count[i] + 1
#
#
# def graf():
#     print(rows, columns)
#     # print(ranNum)
#     # print(count)
#     os.system('clear')
#     x = 0
#     for i in count:
#         te = (max(count) + 20)
#         fe = 0
#         #print(te)
#         if te > int(columns):
#             while te > int(columns):
#                 fe = fe + 10
#                 te = math.ceil(i / fe)
#         else:
#             te = i
#         #print(te)
#
#         print("#" * te, i)
#         # print(x, "#" * (i - len(str(x)) - 1))
#         # print("#" * i, str((i / loop) * 100) + "%")
#         print("")
#
#         # if (max(count) + 20) < int(columns):
#         #     print("#" * i, i)
#         #     print(x, "#" * (i - len(str(x)) - 1))
#         #     print("#" * i, str((i / loop) * 100) + "%")
#         #     print("")
#         # else:
#         #     print("to loong")
#
#
#         x = x +1
#     print(count)
#     print(rows, columns)
#     print(max(count) + 20)
#     #print(ranNum)
#     time.sleep(1)
#
#
#
# # print(rows, columns)
#
# ran()
# makeCount()
# #graf()
#
# # print(ranNum)
# # print(count)
#
# # for i in range(loop):
# #     num.append(random.randrange(0, 10))
# #
# # for i in num:
# #     print(i)
# # def ran():
# #     numList = [0,0,0,0,0,0,0,0,0,0]
# #
# #     for i in range(loop):
# #         ranNum = random.randrange(0, 10)
# #         numList[ranNum] = numList[ranNum] + 1
# #         if (i + 1) % 10 == 0:
# #             for x in range(10):
# #                 #print(x, numList[x], ((numList[x] / (i+1)) * 100), (numList[x] - (/(i+1))))
# #
# #
# # ran()
# # def ran():
# #     numList = [0,0,0,0,0,0,0,0,0,0]
# #     start_time = time.time()
# #     global ranTime
# #     for i in range(loop):
# #         ranNum = random.randrange(0, 10)
# #         numList[ranNum] = numList[ranNum] + 1
# #         if i % 9 == 0 and i > 0:
# #             for x in range(10):
# #                 print(str(x), numList[x], (numList[x] / i) * 100)
# #             print(numList)
# #
# #     ranTime = time.time() - start_time
# # ran()
#
# # print(1 % 10, 2 % 10, 20 % 10)
# #
# #
# # for i in range(1000):
# #     if i % 50 == 0:
# #         print(i)
#
# # for x in range(loop):
# #     ranNum = random.randrange(0, 10)
# #     numList[ranNum] = numList[ranNum] + 1
# #     if x % 10 == 0:
# #         idkidk = 0
# #         idk = 0
# #         for y in range(10):
# #             idk = (numList[y] / loop) * 100
# #             print(y, numList[y], idk)
# #             idkidk = idkidk + idk
# #         print(idkidk)
# #         print("")
#
# # for x in range(10):
# #     idk = (numList[x] / loop) * 100
# #     print(x, numList[x], idk)
# #     idkidk = idkidk + idk
# #     #print("[" + str(x) + " " + str(numList[x]) + "] ", end='')
