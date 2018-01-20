# author     :  Tyler M
# email      :  tylerssspam - gmail 
# date       :  Jan '18

# name       :  kclosestpoints(points,k,closest)
# function(s):  pythagorean theorem, min/max heap sort
# description:  this function will calculate the distance between the origin (0,0)
#               and the given coordinates (x,y) on a 2d grid.  the function will return
#               (k) number of coordinates (and their distances) that are 
#               nearest or farthest from the origin
# parameters :  points - list of tuples [(X1,Y1),(X2,Y2),...(Xn,Yn)]
#               k      - integer representing the number of tuples returned
#               closest- integer indicating closest or farthest
# return     :  (k) sorted tuples [(distance1,(x1,y1)),(distance2,(x2,y2)),...]

import math
import heapq

def kclosestpoints(points,k,closest):
  dList = []
  for index in range(0,len(points)):
    x,y = points[index]
    tmp = ( math.sqrt(x**2+y**2),points[index])
    dList.append(tmp)
  heapq.heapify(dList)
  if closest ==2:
    return (heapq.nlargest(k, dList))
  else:
    return (heapq.nsmallest(k, dList))

# function   :  rndCoords(n,lb,ub)
# function(s):  random function
# description:  this function will generate a random set of points on a (x,y) grid
# parameters :  n     - integer - number of points to create
#               lb    - integer - lower bound of x,y coordinates
#               ub    - integer - upper bound of x,y coordinates
# return     :  (n) number tuples [(x1,y1),(x2,y2),...(xn,yn)]

import random

def rndCoords(n,lb,ub):
  tmpPoints = []
  for i in range(1,1+n):
    x = random.randint(lb,ub)
    y = random.randint(lb,ub)
    tmp = (x,y)
    tmpPoints.append(tmp)
  return tmpPoints
    
#   1-  code below drives the other two programs
#   2-  quick n dirty approach -  little input validation and NO error handling
nTup =int(input("how many x,y coords do you want to create?"))
lBou = int(input("lower bound"))
uBou = int(input("upper bound"))
numRes = int(input("how many points do you want to return?"))
nearest = int(input("would you like points (1) nearest or (2) farthest the origin?"))
while lBou <= uBou and numRes <= nTup:
  print (kclosestpoints(rndCoords(nTup,lBou,uBou),numRes,nearest))
  break
else:
    print("watch your inputs")
    print("https://www.youtube.com/watch?v=hpigjnKl7nI")
