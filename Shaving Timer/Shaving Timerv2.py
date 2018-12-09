import tkinter as tk
from tkinter import ttk
import arrow
import csv

win = tk.Tk()
win.title("Python GUI")
dates = []
newdates = []


def infoDisplay():

    newdates = []

    with open('shaves.txt', 'r') as csvfile:
        readers = csv.reader(csvfile, delimiter=",")
        for row1 in readers:
            newdates.append(row1[1])
            print(row1[1])

    date1 = arrow.get(newdates[len(newdates)-1], 'DD-MM-YYYY')
    date2 = arrow.get(arrow.now().format('DD-MM-YYYY'), 'DD-MM-YYYY')
    diff = date2 - date1

    diffstr = str(diff)
    if str(diffstr[:2]).isdigit():
        diffsub = diffstr[:2]
    else:
        diffsub = diffstr[:1]

    ttk.Label(win, text="Number of Shaves: " + str(len(newdates))).grid(column=0, row=5)
    ttk.Label(win, text="Your Last Shave was on the " + str(newdates[len(newdates)-1])).grid(column=0, row=6)
    ttk.Label(win, text="Days since last shave: " + diffsub).grid(column=0, row=7)



def average():

    total = 0
    n = 0

    with open('shaves.txt', 'r') as csvfile:
        readers1 = csv.reader(csvfile, delimiter=",")
        for row1 in readers1:
            n += 1
            total = total+int(row1[2])
            print(row1[2])
    avg = total / n
    ttk.Label(win, text=str(avg) + " days").grid(column=0, row=3, columnspan=3)


def newShave():
    f = open('shaves.txt', 'r')
    linelist = f.readlines()
    f.close()
    num = len(linelist)
    nextshavenum = len(linelist) + 1

    dates = []

    with open('shaves.txt', 'r') as csvfile:
        readers = csv.reader(csvfile, delimiter=",")
        for row1 in readers:
            dates.append(row1[1])
            print(row1[1])

    print(dates)

    date1 = arrow.get(dates[num - 1], 'DD-MM-YYYY')
    date2 = arrow.get(arrow.now().format('DD-MM-YYYY'), 'DD-MM-YYYY')
    diff = date2 - date1

    diffstr = str(diff)
    if str(diffstr[:2]).isdigit():
        diffsub = diffstr[:2]
    else:
        diffsub = diffstr[:1]
    print(diffsub)

    f = open('shaves.txt', 'a')
    f.write('\n' + str(nextshavenum) + ',' + arrow.now().format('DD-MM-YYYY') + ',' + diffsub)
    f.close()


NewShaveBtn = ttk.Button(win, text='Ive Shaved', command=newShave).grid(column=0, row=0, columnspan=3)
AverageDaysBtn = ttk.Button(win, text='Average', command=average).grid(column=0, row=1, columnspan=3)

displayBtn = ttk.Button(win, text='Display Info', command=infoDisplay)
displayBtn.grid(column=0, row=4, columnspan=3)

win.mainloop()
