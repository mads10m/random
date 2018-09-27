import random
import time
import threading
import os
import math
import sys
import ast

import file
import analyse

ranNum = []
count = [0,0,0,0,0,0,0,0,0,0]
#count = [1,1,1,1,1,1,1,1,1,1]
percent = []
loop = 1000000

rows, columns = os.popen('stty size', 'r').read().split()

def writeToFile(fileName, content):
    f = open(fileName + ".txt","w+")
    f.write(str(content))
    f.close()

def readFile(fileName):
    f = open(fileName + ".txt", "r")
    f = f.read()
    return(f)

def fileToArray(fileName):
    start_time = time.time()
    file = readFile(fileName)
    array = ast.literal_eval(file)
    print(time.time()-start_time)
    # print(array)


def randomLibary():
    start_time = time.time()
    for i in range(loop):
        ranNum.append(random.randrange(0, 10))
        if (i + 1) % 100 == 0:
            print(str(i) + ":", str(math.floor((i/loop)*100)) + "%", end="\r")
    print(str(i) + "'s time:", time.time()-start_time)
    writeToFile("test", ranNum)

def graf():
    pass

# fileToArray("test")

   # count = 0
   # while count < 5:
   #    time.sleep(delay)
   #    count = count + 1
   #    # print "%s: %s" % ( threadName, time.ctime(time.time()) )
   #    print(threadName, time.ctime(time.time()))

# Create two threads as follows

# print_time("Thread-1", 2)
# t1 = threading.Thread(target=print_time, args=("Thread-1", 2, ))
# # t2 = threading.Thread(target=print_time, args=("Thread-2", 4, ))
# t1.start()
# t1 = threading.Thread(target=print_time, args=("Thread-1", 2, ))
# t2 = threading.Thread(target=print_time, args=("Thread-2", 4, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# thread.start_new_thread(randomLibary, ("Thread-1"))

# try:
#    thread.start_new_thread(randomLibary, ("Thread-1"))
#    thread.start_new_thread(randomLibary, ("Thread-2"))
# except:
#    print "Error: unable to start thread"

# def randomLibary(fileName, loop):
#     for i in range(loop):
#         ranNum.append(random.randrange(0, 10))
#     writeToFile(fileName, ranNum)
    # print(ranNum)
    # print(readFile("test"))

def countList():
    for i in ranNum:
        count[i] = count[i] + 1

def percentage():
    for i in count:
        percent.append(i/loop)
    print(ranNum)
    print(count)
    print(percent)
    t = 0
    for i in percent:
        t = t + i
    print(t)

def analyse():
    # count how many times every number accours
    countList()
    percentage()


# randomLibary()
# analyse()

def init():
    done = 0
    while done == 0:
        newRanNum = input("Generate new random numbers? [y/n] ").lower()
        if newRanNum == "y" or newRanNum == "yes":
            done = 1
        elif newRanNum == "n" or newRanNum == "no":
            something = "no"
            done = 1
        else:
            print("You wrote something else that yes or no")

    if newRanNum == "y" or newRanNum == "yes":
        filename = input("Name of file (don't and .txt) ")
        while filename.isalpha() == False:
            print("The name can only contain letters and no spaces")
            filename = input("Name of file (don't and .txt) ")

        loop = input("How many random numbers you want generatet? ")
        while loop.isdigit() == False:
            print("That is not a number")
            print(loop)
            loop = input("How many random numbers you want generatet? ")
        loop = int(loop)

        randomLibary(filename, loop)

# init()

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
