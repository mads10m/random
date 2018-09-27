import os
import time
import math

import file
import generate
import analyse

# Gets the length and height of the terminal
rows, columns = os.popen('stty size', 'r').read().split()

#
yes = ["yes", "y"]
no = ["no", "n"]

##
## YOU CAN CAHNGE WHILE LOOP. JUST CALL IT Somthing == True AND THEN USE BRAK
##

def analyse_numbers():
    try:
        answer = False
        while answer == False:
            analyse_file = input("Do you want to analyse " + file_name + "? [y/n] ")
            if analyse_file in yes:
                answer = True
                analyse.all(file_name)
            elif analyse_file in no:
                break
            else:
                print("Invalid input")
    except NameError:
        answer = False
        while answer == False:
            analyse_file = input("Which file do you want to analyse? ")
            if os.path.isfile(analyse_file + ".txt") == False:
                print(analyse_file + " do not exists")
            else:
                answer = True
                analyse.all(analyse_file)

def generate_numbers():
    global file_name

    # Asks questions to get the file name
    rename = False
    while rename == False:
        file_name = input("Name of file (don't add .txt) ")
        if os.path.isfile(file_name + ".txt") == True:
            answer = False

            while answer == False:
                overwrite = input(file_name + ".txt does already exists. Do you want to overwrite it? [y/n] ").lower()
                if overwrite in yes:
                    answer = True
                    rename = True
                elif overwrite in no:
                    answer = True

                else:
                    print("Invalid input")
        elif file_name.isspace() == True:
            print("Invalid input")
        else:
            rename = True

    num_of_random = input("How many random numbers you want generatet? ")
    while num_of_random.isdigit() == False:
        print("Invalid input")
        num_of_random = input("How many random numbers you want generatet? ")

    num_of_random = int(num_of_random)

    generate.randomArray(file_name, num_of_random)
    analyse_numbers()



answer = False
while answer == False:
    gen_new_num = input("Generate new random numbers? [y/n] ").lower()
    if gen_new_num in yes:
        answer = True
        generate_numbers()
    elif gen_new_num in no:
        answer = True
        analyse_numbers()
    else:
        print("Invalid input")



# fileName = None
#
# def genRan():
#     answer = False
#     global fileName
#     fileName = input("Name of file (don't add .txt) ")
#     while answer == False:
#         if os.path.isfile(fileName + ".txt") == True:
#             overwrite = input(fileName + ".txt does already exists. Do you want to overwrite it? [y/n] ").lower()
#             if overwrite == "y" or overwrite == "yes":
#                 answer = True
#             elif overwrite == "n" or overwrite == "no":
#                 fileName = input("Name of file (don't add .txt) ")
#                 if os.path.isfile(fileName + ".txt") == False:
#                     answer = True
#             else:
#                 print("Invalid input")
#                 overwrite = input(fileName + ".txt does already exists. Do you want to overwrite it? [y/n] ").lower()
#         else:
#             answer = True
#
#     numOfRan = input("How many random numbers you want generatet? ")
#     while numOfRan.isdigit() == False:
#         print("Invalid input: Can only be a number!")
#         numOfRan = input("How many random numbers you want generatet? ")
#     numOfRan = int(numOfRan)
#     generate.randomArray(fileName, numOfRan)
#
# answer = False
# genNewNum = input("Generate new random numbers? [y/n] ").lower()
# while answer == False:
#     if genNewNum == "y" or genNewNum == "yes":
#         answer = True
#         genRan()
#     elif genNewNum == "n" or genNewNum == "no":
#         answer = True
#         print("no:", genNewNum)
#     else:
#         print("Invalid input")
#         genNewNum = input("Generate new random numbers? [y/n] ").lower()
#
# answer = False
# if fileName != None:
#     analyseFile = input("Do you want to analyse " + fileName + ".txt? [y/n] ").lower()
#     while answer == False:
#         if analyseFile == "y" or analyseFile == "yes":
#             print("Analysing", fileName + ".txt")
#             analyse.all(fileName)
#             answer = True
#         elif analyseFile == "n" or analyseFile == "no":
#             answer = True
#             analyseFile = input("Witch file then? (don't add .txt) ")
#             if os.path.isfile(analyseFile + ".txt") == True:
#                 print("Analyse", analyseFile + ".txt")
#                 # analyse.
#             else:
#                 print("Somthing when wrong")
#         else:
#             print("Invalid input")
#             analyseFile = input("Do you want to analyse", fileName + ".txt? [y/n] ").lower()
# else:
#     analyseFile = input("Witch file do you want to analyse? ")
#     analyse.all(analyseFile)





# def yesNo(question, ifYes, ifNo):
#     yes = ["y", "yes"]
#     no = ["n", "no"]
#     answer = False
#     while answer == False:
#         test = input(question).lower()
#         if test in yes:
#             answer = True
#             ifYes()
#         elif test in no:
#             answer = True
#             ifNo()
#         else:
#              print("Invalid input")
#
#
# def testtt():
#     print("ye")
#
# yesNo("test [y/n] ", testtt, "no")

# for i in range(1000):
#     progressBar.proBar(i, 1000)
    # rows, columns = os.popen('stty size', 'r').read().split()
    # i = i + 1
    # pro = str(math.floor((i/100)*100)) + "% "
    # if len(pro) == 3:
    #     tf = 5
    # elif len(pro) == 4:
    #     tf = 6
    # else:
    #     tf = 7
    # lenn = int(columns)-tf
    # idkkk = math.floor((i/100) * lenn)
    # prolenn = "=" * idkkk
    # space = " " * ((int(columns) - idkkk) - tf)
    #
    # # print(prolenn)
    #
    # tt = "=" * i
    # ss = " " * (lenn - i)
    # if i == 100:
    #     print(pro + "[" + prolenn + "]")
    # else:
    #     print(pro + "[" + prolenn + space + "]", end="\r")
    # time.sleep(0.1)
