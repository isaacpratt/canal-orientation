#Amira Lineset subsampler

#subsampler written in python
#trying to keep code analagous to imagej macro
#differences will be noted
#Copyright (C) 2017  Isaac Pratt
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#v0 Started 8/03/2017
#v1 Finished 10/03/2017
#v2 Now works by selecting folder with linesets inside
#v2 Finished 26/06/2017


import os

import numpy as np
#numpy for calculations

from Tkinter import *
from tkFileDialog import *
#tkinter for file dialogs

import time
from tqdm import *
#tqdm for progress bar


#CHANGE THE PARAMETERS HERE
#INTERVAL IN MICRONS
#LINESETS OPTION NOT YET IMPLEMENTED
interval = 10
linesets = 1

root = Tk()
root.withdraw()

root.lift()
root.focus_force()


#choose folder
directory = askdirectory()

root.destroy()

file_paths = os.listdir(directory)
print file_paths

counter=0
for filepath in file_paths:
    print "direct", directory
    print filepath

    NewFileName = filepath.split('.', 2)[0] + ".Subsample" + ".txt"

    RawString = open(directory+"/"+filepath)

    NewFile = open(NewFileName, "w+")
    NewFile.write("# LineSet 0.1\n\nnDataVals 1\n\n{ {\n")

    #cuts off the header from the lineset

    #split the lineset string using between canal lines in the lineset

    LineStrings = RawString.read().split(' {')
    #cuts off the header from the lineset
    Lines = []
    floatLines = []
    del LineStrings[0]
    #del LineStrings[-1]

    for i in range(len(LineStrings)):
        Lines.append(LineStrings[i].splitlines())
    
    for line in Lines:
        del line[0]
        del line[-1]

    del line[-1]

    NewString1 = ''
    NewString2 = ''

    print "number of lines",len(LineStrings)

    pbar = tqdm(total=len(LineStrings), leave=True)
    
    #iterate over all canal lines
    for i in range(len(LineStrings)):
        #print "------------------------------i ",i
        #iterate over an individual canal
        Points = []
        for j in range(len(Lines[i])):
            #print "j ",j
            #get point coordinates
            xCoord, yCoord, zCoord, garbage = str(Lines[i][j]).split() 
            #np.append(Points, [float(xCoord), float(yCoord), float(zCoord)])
            Points.append([xCoord, yCoord, zCoord])
        npPoints = np.asarray(Points).astype(np.float)
        npPoints = np.round(npPoints, decimals = 1)
        l = 0
        for k in range(len(Lines[i])):
            if l < len(Lines[i])-1:
                for l in range(len(Lines[i])):
                    #do the calculation - http://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
                    PointDistance = np.linalg.norm(npPoints[l]-npPoints[k])
                    #if the 3d distance is greater than or equal to the interval, write line k and line l as the new 'subsampled' line segment
                    if PointDistance >= interval:
                        #print PointDistance
                        StringPoint = np.array2string(npPoints[k], formatter={'float_kind':'{0:.1f}'.format})[1:-1]
                        #StringPoint = " ".join(str(npPoints[k])[2:-2].split())
                        NewFile.write(StringPoint+"\n")
                        #print "greater than ", NewString1
                        StringPoint2 = np.array2string(npPoints[l], formatter={'float_kind':'{0:.1f}'.format})[1:-1]
                        #StringPoint2 = " ".join(str(npPoints[l])[2:-2].split())
                        NewFile.write(StringPoint2+"\n")
                        NewFile.write("} {\n")
                        #set the new first line to the previous second line
                        k = l
        
                    if  l == len(Lines[i])-1:
                        #print "equals",
                        StringPoint3 = np.array2string(npPoints[k], formatter={'float_kind':'{0:.1f}'.format})[1:-1]
                        #StringPoint3 = " ".join(str(npPoints[k])[2:-2].split())
                        NewFile.write(StringPoint3+"\n")
                        StringPoint4 = np.array2string(npPoints[l], formatter={'float_kind':'{0:.1f}'.format})[1:-1]
                        #StringPoint4 = " ".join(str(npPoints[l])[2:-2].split())
                        NewFile.write(StringPoint4+"\n")
                        if i == len(LineStrings)-1:
                            NewFile.write("}")
                        else: NewFile.write("} {\n")
                        k = l
                        break
                    pbar.update(1)
            

    pbar.close()
    NewFile.write("\n}\n")
    NewFile.close()
    RawString.close()

    #print "Lineset finished "&counter&" out of "&len(file_paths)
    counter+=1
    print "Report closed ", counter, " out of ", len(file_paths)
    print 
    #print LineStrings[0]



#from http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1