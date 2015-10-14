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
    print lift
    print drag
    print liftdrag
#Only to make testing easier
#liftdragratio('drag_ligt.m')