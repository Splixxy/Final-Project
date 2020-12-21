import os
import os.path
import random
import re
import tkinter as tk
from tkinter.ttk import *
path = input("Please input the path to the question & answer file:")
isFile = os.path.exists(path)
isFileSTR = str(isFile)
increase = 0
correct = 0
def V(increase):
    global Vlist
    Vlist = VDict
    global QT
    global QA
    global QC
    global QCA
    global QCB
    global QCC
    global QCD
    QT = "%s" % increase
    QA = "%sAnswer" % Vlist[increase]
    QC = "%s" % Vlist[increase]
    QCA = "%sA" % Vlist[increase]
    QCB = "%sB" % Vlist[increase]
    QCC = "%sC" % Vlist[increase]
    QCD = "%sD" % Vlist[increase]
    print(Vlist)
def counter():
    global increase
    if increase < qcount:
        increase = increase + 1
    else:
        scoreWindow()

def scoreWindow():
    newWindow = tk.Toplevel(window)
    newWindow.title("Final Score")
    newWindow.rowconfigure(0, minsize=200, weight=1)
    newWindow.columnconfigure([0, 2], minsize=200, weight=1)
    greeting = tk.Label(master=newWindow, text="You have finished the quiz", bg="skyblue")
    greeting.grid(row = 0, column = 1)
    greeting1 = tk.Label(master=newWindow, text="You scored a %d/%d" % (correct,qcount), bg="skyblue")
    greeting1.grid(row = 1, column = 1)
    CQButton = tk.Button(master=newWindow,text = "Close Quiz", fg = "black", command = closeWindow)
    CQButton.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
    newWindow.mainloop()

def ContinueWindow():
    counter()
    V(increase)
    Q = next( v for k,v in QDict.items() if k.startswith(QC))
    Q1 = next( v for k,v in QDict.items() if k.startswith(QCA))
    Q2 = next( v for k,v in QDict.items() if k.startswith(QCB))
    Q3 = next( v for k,v in QDict.items() if k.startswith(QCC))
    Q4 = next( v for k,v in QDict.items() if k.startswith(QCD))
    QL = len(Q)
    print(Q)
    newWindow = tk.Toplevel(window)
    newWindow.title("Question %s" % QT)
    newWindow.rowconfigure(0, minsize=200, weight=1)
    newWindow.columnconfigure([0, 2], minsize=200, weight=1)
    greeting = tk.Label(master=newWindow, text=Q[1:QL], bg="skyblue")
    greeting.grid(row = 0, column = 1)
    Q1Button = tk.Button(master=newWindow,text = Q1[1], fg = "black", command = CheckQuestion1)
    Q1Button.grid(row = 2, column = 0, sticky= "nsew", padx = 5, pady = 5,)
    Q2Button = tk.Button(master=newWindow,text = Q2[1], fg = "black", command = CheckQuestion2)
    Q2Button.grid(row = 2, column = 2, sticky= "nsew", padx = 5, pady = 5,)
    Q3Button = tk.Button(master=newWindow,text = Q3[1], fg = "black", command = CheckQuestion3)
    Q3Button.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
    Q4Button = tk.Button(master=newWindow,text = Q4[1], fg = "black", command = CheckQuestion4)
    Q4Button.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
    newWindow.mainloop()
def openNewWindow():
    V(increase)
    Q = next( v for k,v in QDict.items() if k.startswith(QC))
    Q1 = next( v for k,v in QDict.items() if k.startswith(QCA))
    Q2 = next( v for k,v in QDict.items() if k.startswith(QCB))
    Q3 = next( v for k,v in QDict.items() if k.startswith(QCC))
    Q4 = next( v for k,v in QDict.items() if k.startswith(QCD))
    QL = len(Q)
    newWindow = tk.Toplevel(window)
    newWindow.title("Question %s" % QT)
    newWindow.rowconfigure(0, minsize=200, weight=1)
    newWindow.columnconfigure([0, 2], minsize=200, weight=1)
    greeting = tk.Label(master=newWindow, text=Q[1:QL], bg="skyblue")
    greeting.grid(row = 0, column = 1)
    Q1Button = tk.Button(master=newWindow,text = Q1[1], fg = "black", command = CheckQuestion1)
    Q1Button.grid(row = 2, column = 0, sticky= "nsew", padx = 5, pady = 5,)
    Q2Button = tk.Button(master=newWindow,text = Q2[1], fg = "black", command = CheckQuestion2)
    Q2Button.grid(row = 2, column = 2, sticky= "nsew", padx = 5, pady = 5,)
    Q3Button = tk.Button(master=newWindow,text = Q3[1], fg = "black", command = CheckQuestion3)
    Q3Button.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
    Q4Button = tk.Button(master=newWindow,text = Q4[1], fg = "black", command = CheckQuestion4)
    Q4Button.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
    newWindow.mainloop()
def CheckQuestion1():
    Q1 = next( v for k,v in QDict.items() if k.startswith(QCA))
    QAnswer = next( v for k,v in QDict.items() if k.startswith(QA))
    if Q1[1] == QAnswer[1]:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question correctly", bg="green")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)
        global correct
        correct = correct + 1
    else:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question incorrectly", bg="red")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)

def CheckQuestion2():
    Q2 = next( v for k,v in QDict.items() if k.startswith(QCB))
    QAnswer = next( v for k,v in QDict.items() if k.startswith(QA))
    if Q2[1] == QAnswer[1]:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question correctly", bg="green")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)
        global correct
        correct = correct + 1
    else:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question incorrectly", bg="red")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)

def CheckQuestion3():
    Q3 = next( v for k,v in QDict.items() if k.startswith(QCC))
    QAnswer = next( v for k,v in QDict.items() if k.startswith(QA))
    if Q3[1] == QAnswer[1]:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question correctly", bg="green")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)
        global correct
        correct = correct + 1
    else:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question incorrectly", bg="red")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)

def CheckQuestion4():
    Q4 = next( v for k,v in QDict.items() if k.startswith(QCD))
    QAnswer = next( v for k,v in QDict.items() if k.startswith(QA))
    if Q4[1] == QAnswer[1]:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question correctly", bg="green")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)
        global correct
        correct = correct + 1
    else:
        newWindow = tk.Toplevel(window)
        newWindow.title("Question Check")
        newWindow.rowconfigure(0, minsize=200, weight=1)
        newWindow.columnconfigure([0, 2], minsize=200, weight=1)
        greeting = tk.Label(master=newWindow, text="You answered this question incorrectly", bg="red")
        greeting.grid(row = 0, column = 1)
        yesButton = tk.Button(master=newWindow,text = "Continue Quiz", fg = "black", command = ContinueWindow)
        yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
        noButton = tk.Button(master=newWindow,text = "End Quiz", fg = "black", command = closeWindow)
        noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
        submitButton = tk.Button(master=newWindow,text = "Submit Quiz", fg = "black", command = scoreWindow)
        submitButton.grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)

def closeWindow():
    window.destroy()

def fileSearch (qcount):
    count = 0
    for x in range(0,qcount):
        count = count + 1
        QDict = dict()
        with open("Question-Answer.txt", "r") as fOpen:
            for line in fOpen:
                name = line.split()[0]
                question = line.split()
                if name not in QDict:
                    QDict[name] = question
    return QDict;

def DictList(qcount):
    VDict = []
    for i in range(1000):
        int = random.randint(0,qcount - 1)
        if int not in VDict: VDict.append(int)
    return VDict;
if isFileSTR == "True":
    qcount = input("Please input the amount of questions on this quiz:")
    qcount = int(qcount)
    VDict = DictList(qcount)
    QDict = fileSearch(qcount)
    LQDict = list(QDict.values())
    window = tk.Tk()
    window.title("Quiz Machine")
    window.rowconfigure(0, minsize=200, weight=1)
    window.columnconfigure([0, 2], minsize=200, weight=1)
    txt_edit = tk.Text(window)
    frame = tk.Frame(master=window, width=150, height=150)
    greeting = tk.Label(master=window, text="Press (YES) if you would like to start the quiz", bg="skyblue")
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
