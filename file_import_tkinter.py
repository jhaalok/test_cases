import tkinter
import re
import os
from tkinter import ttk
from tkinter.filedialog import askopenfile
import math
import numpy
import numpy as np
import matplotlib.pyplot as plt

root = tkinter.Tk()
root.withdraw()
root.file = askopenfile(mode = 'r')
indata = root.file.readlines()[15:]
floatdat = [indata]
####float_dat = [int(x) for x in floatdat]
print(floatdat)
#for line in indata:
#    for number_str in line.split():
#        number = float(number_str)
#print(number)
        ####if (number > 0)
            ###numbers.append(number)
#print (indata)
#plt.subplot(data)