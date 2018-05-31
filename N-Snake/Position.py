# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:26:17 2018

@author: Isik
"""

class Position:
    """
    Represents position in N dimensions
    Is designed to be able to have a direction added to it.
    
    --------------------------------------------------------------------------
    properties
    --------------------------------------------------------------------------
    coordinates:    List of integers
        Each integer represents a position in space. The index + 1 is the dime-
        nsion represented by the value.
    """
    def __init__(self, coordinates = []):
        self.coordinates = coordinates[:]
        
    def __add__(self, direction):
        """
        Addition definition for position
        NOTE: is only supposed to have a direction type object used here.
        """
        localCoordinates = self.coordinates[:]
        for i in range( len(localCoordinates), len(direction.directionalCoordinates) ):
            localCoordinates.append(0)
        for index, dirCoord in enumerate(direction.directionalCoordinates):
            localCoordinates[index] += dirCoord
            
        return Position(localCoordinates)


    def __eq__(self, other):
        if isinstance(self, other.__class__):
            for cSelf, cOther in zip(self.coordinates, other.coordinates):
                if cSelf != cOther:
                    return False
            return True
        return False