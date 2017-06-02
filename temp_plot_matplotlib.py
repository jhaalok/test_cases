#!/usr/bin/env python
#!/usr/local/lib/python3 

import tkinter
import re
import os
from tkinter import ttk
from tkinter.filedialog import askopenfile
import numpy as np
import matplotlib.pyplot as plt
root = tkinter.Tk()
root.withdraw()
filename = askopenfile(title = '@@@@@@@@ FUEL PLOTS @@@@@@@@@' , mode='r')
name = os.path.splitext(os.path.basename(filename.name))[0]
#print(name)
######## Convert string data read from file to float for plotting #########

indata = filename.readlines()[15:]
for line in indata:
    for number_str in line.split()[1:]:
        for number_str1 in line.split()[:1]:
            x = number1 = float(number_str1)
            y = number = float(number_str)
           #print(x)
           #print (y)

#A = [map(float,num.split()) for num in filename.readlines()[15:]]
  
######### Plot utility using matplotlib ######## 
#print(A)
#tx = np.arange(x, dtype=np.float32)
#ty = np.arange(y, dtype=np.float32)
#print(t)
plt.plot([y])
#plt.axis([tx])
plt.legend()
plt.show()



