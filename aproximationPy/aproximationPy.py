from mnq import Mnq
from lagrng import Lagrng
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

# check inputed values for numeric
def check_fields():
    inpdata = []
    yfloat = []
    inpdata.append(y1.get())
    inpdata.append(y2.get())
    inpdata.append(y3.get())
    inpdata.append(y4.get())
    inpdata.append(y5.get())
    for y in inpdata:
        try:
            yfloat.append(float(y))
        except Exception as e:
            print(e)
            return
    # plot if ok
    run_plot(yfloat)
    
# draw aproximated functions, y - inputed points values
def run_plot(y):
    points = dict({1: y[0], 2: y[1], 3: y[2], 4: y[3], 5: y[4]}) 
    
    mq = Mnq(points)
    lg = Lagrng(points)

    xlist = np.arange(0, 6, 0.1)
    yMNQlist = [mq.mnq_aprox_function(x) for x in xlist]
    yLaGrnglist = [lg.lagrng_aprox_function(x) for x in xlist]
    
    plt.plot(xlist, yMNQlist, label='MNQ', linewidth=3.0)
    plt.plot(xlist, yLaGrnglist, label='LaGrange')
    plt.plot(points.keys(), points.values(), marker = 'o', linestyle='None', label='points')
    plt.legend()
    plt.show()

# create input window
master = Tk()
Label(master, text="y (1) = ").grid(row=1)
Label(master, text="y (2) = ").grid(row=2)
Label(master, text="y (3) = ").grid(row=3)
Label(master, text="y (4) = ").grid(row=4)
Label(master, text="y (5) = ").grid(row=5)

y1 = Entry(master)
y2 = Entry(master)
y3 = Entry(master)
y4 = Entry(master)
y5 = Entry(master)

y1.grid(row=1, column=1)
y2.grid(row=2, column=1)
y3.grid(row=3, column=1)
y4.grid(row=4, column=1)
y5.grid(row=5, column=1)

Button(master, text='Plot', command=check_fields).grid(row=7, column=1, sticky=W, pady=4)

# run input window
mainloop( )

