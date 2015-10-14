import operator
import os
def liftdragratio(filename):
  numberofLines = 0
  lift = 0.0
  drag = 0.0
  with open(filename) as f:
    next(f) #Skip header
    for line in f:
      splitLine = line.split('\t')
      splitLine[1]
      lift += float(splitLine[1])
      drag += float(splitLine[2])
      numberofLines+=1
    #Get the mean value
    lift = lift/numberofLines
    drag = drag/numberofLines
    liftdrag = lift/drag
    #print filename
    #print liftdrag
    dict = {filename: liftdrag}
    return dict
#Only to make testing easier
#liftdragratio('drag_ligt.m')

#Take angle.m from 0-num
def findOptimal(folder):
  angles = {}
  anglesTest = {'0.m':3237, '3.m':6984, '6m':3900}
  for f in os.listdir(folder):
    #add check to only do this for .m files
    if f.endswith(".m"):
      angles.update(liftdragratio(folder + '/' + f))
  print angles
  print max(angles, key=angles.get)