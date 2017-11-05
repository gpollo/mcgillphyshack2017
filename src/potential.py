#!/usr/bin/env python3
"""
Created on Sat Nov  4 10:10:48 2017

@author: utilisateur1
"""
import math, numpy, time
import matplotlib # for changing the matplotlib.contour behavior
import matplotlib.pyplot as plt

from constants import *

def main ():
    plt.ion()
    planetTest = TestCelestialObject(5000*10**(4),5000*10**(4),2*10**(30))
    planetTest2 = TestCelestialObject(7000*10**(4),6000*10**(4),4*10**(30))
    planetTest3 = TestCelestialObject(10000*10**(4),15000*10**(4),3.5*10**(30))
    planetTest3 = TestCelestialObject(15000*10**(4),15000*10**(4),2*10**(30))
    planetTest4 = TestCelestialObject(6000*10**(4),12000*10**(4),7*10**(30)) 
    objectList=[]
    objectList.append(planetTest)
    objectList.append(planetTest2)
    objectList.append(planetTest3)
    objectList.append(planetTest4)
    
    potential = Potential(1500*10**(3))
    
    potentialFigure = plt.figure('3d view')
    
    potential.compute(objectList, -10**(8), 10**(8), -10**(8), 10**(8))
    potential.initialisePlot(potentialFigure)
    potential.actualisePlot()
    
    planetTest5 = TestCelestialObject(4000*10**(4),16000*10**(4),4.3*10**(30))
    planetTest6 = TestCelestialObject(14000*10**(4),7000*10**(4),1.5*10**(30))
    objectList.append(planetTest5)
    objectList.append(planetTest6)
    
    potential.compute(objectList, -10**(8), 10**(8), -10**(8), 10**(8))
    time.sleep(0.01)
    potential.actualisePlot()
    
    planetTest7 = TestCelestialObject(6000*10**(4),4500*10**(4),5.3*10**(30))
    planetTest8 = TestCelestialObject(20000*10**(4),3000*10**(4),33.5*10**(30))
    objectList.append(planetTest7)
    objectList.append(planetTest8)
    
    potential.compute(objectList, -10**(8), 10**(8), -10**(8), 10**(8))
    time.sleep(0.01)
    potential.actualisePlot()
    time.sleep(0.01)
    
    del potentialFigure

# defining a function that compute the distance between a celestial object (from that class) and a point
"""Definition________________________________________________"""
def distanceCompute(celestialObject, position_x, position_y):
    delta_x = celestialObject.x-position_x
    delta_y = celestialObject.y-position_y
    distance = math.sqrt(delta_x**2 + delta_y**2)
    return distance
"""__________________________________________________________________"""

class TestCelestialObject(object):
    def __init__(self, x,y,m):
        self.x=x
        self.y=y
        self.m=m
        print("celestial object class ok")

class Potential(object):
    def __init__(self, delta):
        self.delta = delta
        
    def compute(self, objectList, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.x_list = numpy.arange(x_min-self.delta, x_max+self.delta, self.delta)
        self.y_list = numpy.arange(y_min-self.delta, y_max+self.delta, self.delta)
        
        self.potentialMatrix = numpy.zeros( (len(self.x_list), len(self.y_list)) )
        
        # for each point on the discretization of space: (double for)
        for iterate_x in range(0,len(self.x_list)) :
            position_x = self.x_list[iterate_x]
            for iterate_y in range(0,len(self.y_list)) :
                position_y = self.y_list[iterate_y]
                # adding the potential from each celestial object contained in objectList
                for i in range(0, len(objectList)):
                    distance_i = distanceCompute(objectList[i], position_x, position_y)
                    if distance_i ==0:
                        self.potentialMatrix[iterate_x, iterate_y] = self.potentialMatrix[iterate_x-1, iterate_y-1]
                    else:
                        addPotential = -(G/(distance_i))*(objectList[i].m)
                        self.potentialMatrix[iterate_x, iterate_y] = self.potentialMatrix[iterate_x, iterate_y] + addPotential
        print("compute executed, ok")
        
    def initialisePlot(self, potentialFigure):
        # we now define the plot for the potential with matplotlib
        self.potentialFigure = potentialFigure
        self.potentialFigure.ax = potentialFigure.add_subplot(1,1,1)
        print("subplot initialised")
        
        matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
        self.coloring =  self.potentialFigure.ax.imshow(self.potentialMatrix, interpolation='bilinear', cmap='spectral', extent= [self.x_min, self.x_max, self.y_min, self.y_max], animated=True)     
        self.lines = self.potentialFigure.ax.contour(self.potentialMatrix, linewidths=1, colors='k', animated=True)
        self.colorbar = plt.colorbar(self.coloring, shrink=0.8, extend='both')
        print("lines and coloring initialised")
        
        self.potentialFigure.ax.set_xlabel("x (m)")
        self.potentialFigure.ax.set_ylabel("y (m)")
        plt.show()
        
    def actualisePlot(self):
        # actualise the plot
        #self.lines.set_zdata(self.potentialMatrix)
        self.coloring.set_data(self.potentialMatrix)
        self.potentialFigure.canvas.draw()
        print("runned through the actualisePlot method")
        
            
if __name__ == "__main__":
    main()
        
    
        
