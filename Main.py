import os
import os.path
import random
import re
import tkinter as tk
from tkinter.ttk import *
path = input("Please input the path to the question & answer file:")
isFile = os.path.exists(path)
isFileSTR = str(isFile)
def openNewWindow():
    newWindow = tk.Toplevel(window)
    newWindow.title("Question 1")
    newWindow.geometry("200x200")
    newWindow.mainloop()

def closeWindow():
    window.destroy()

def fileSearch (VDict,qcount):
    c = 0
    QDict = dict()
    dictValues = VDict.values()
    dictQList = list(dictValues)
    dictQList = str(dictQList[c])
    count = 0
    while count < qcount:
        count = count + 1
        with open("Question-Answer.txt", "r") as fOpen:
            for line in fOpen:
                if re.search(dictQList,line):
                    name = line.split()[0]
                    question = line.split()[1]
                    if name not in QDict:
                        QDict[name] = question
    return QDict;
def qCounter(qcount):
    count = 0
    intD = dict()
    while count < qcount:
        rINT = str(random.randint(0,qcount))
        while rINT not in intD:
            if rINT not in intD:
                intD[rINT] = rINT
                count = count + 1
            else:
                rInt = random.randint(0,qcount)
    return intD;
def DictList(intD,qcount):
    VDict = dict()
    dictValues = intD.values()
    dictVList = list(dictValues)
    c = 0
    for x in range(0,qcount):
        VDict[dictVList[c]]= x
        c = c + 1
    return VDict;
if isFileSTR == "True":
    qcount = input("Please input the amount of questions on this quiz:")
    qcount = int(qcount)
    intD = qCounter(qcount)
    VDict = DictList(intD,qcount)
    print(VDict)
    print(VDict.values())
    QDict = fileSearch(VDict,qcount)
    print(QDict)
    window = tk.Tk()
    window.title("Quiz Machine")
    window.rowconfigure(0, minsize=200, weight=1)
    window.columnconfigure([0, 2], minsize=200, weight=1)
    txt_edit = tk.Text(window)
    frame = tk.Frame(master=window, width=150, height=150)
    greeting = tk.Label(master=window, text="Press (YES) if you would like to start the quiz", bg="red")
    greeting.grid(row = 0, column = 1)
    yesButton = tk.Button(master=window,text = "YES", fg = "black", command = openNewWindow)
    yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
    noButton = tk.Button(master=window,text = "NO", fg = "black", command = closeWindow)
    noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
    window.mainloop()
else:
    QACount = input("Please input how many questions you would like to have on the quiz:")
    QACount = int(QACount)
    QACounter = 0
    while QACounter < QACount:
        QV = str(QACounter)
        QAFile = open("Question-Answer.txt" , "a")
        QAFile.write("%s:\n%sA:\n%sB:\n%sC:\n%sD:\n%sAnswer:\n" % (QV,QV,QV,QV,QV,QV))
        QAFile.close()
        QACounter = QACounter + 1
    print("Question-Answer.txt has been created.")
    print("Now Exiting, Please rerun when question & answers have been inputed")
    exit()
