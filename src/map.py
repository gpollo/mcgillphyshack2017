#!/usr/bin/env python3

#Importing packages
from celestial_object import*
from constants import*
from planet import*
from potential import*
from rocket import*
import numpy as np

#Defining constants
dt = 500

class Map():

    def __init__(self, objectList, rocket=None):
        self.objectList = objectList
        self.rocket = rocket

    def getList(self):
        return self.objectList

    def getRocket(self):
        return self.rocket

    def getLimitsX(self):
        return min([space_object.x for space_object in self.objectList.values() ]),\
               max([space_object.x for space_object in self.objectList.values() ])

    def getLimitsY(self):
        return min([space_object.y for space_object in self.objectList.values()]),\
               max([space_object.y for space_object in self.objectList.values() ])

    def Step(self):
        #Updating all acceleration:
        # 1) for all planets
        for objetSpatial in self.objectList.values():
            objetSpatial.acceleration(self.objectList)

        # 2) for the rocket
        if self.rocket:
            self.rocket.acceleration(self.objectList)

        #Update the data of all the objects
        # 1) For the planets
        for objetSpatial in self.objectList.values():
            objetSpatial.actualizeSystem(dt)
            objetSpatial.actualizeAngle(dt)

        # 2) For the rocket
        if self.rocket:
            self.rocket.actualizeSystem(dt)

        #Deal with the collision
        # 1) For the planets
        # i) Construct a list of all the tuple of the planets that collided
        index_collision = []
        for objectSpatial in self.objectList.values():
            if (objectSpatial.collision) and (not objectSpatial.index in [ j for i,j in index_collision ]):
                for index_col in objetSpatial.collision:
                    index_collision.append(( objetSpatial.index, index_col ))

        # ii) For all the collided planet define a new one and erase the collided ones
        if index_collision:
            for i,j in index_collision:
                self.objectList[i].collide(self.objectList[j])
                del self.objectList[j]

        # 2) For the rocket
        if self.rocket:
            if self.rocket.collision:
                return True


