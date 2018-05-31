# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:40:14 2018

@author: Isik
"""

class Direction:
    """
    An object for keeping track of what direction the snake is headed.
    
    --------------------------------------------------------------------------
    Properties:
        directionalCoordinates - list of integers
            Describes which direction the snake will go from the perspective of
            the head. Each value should be 1, 0, or -1 and at least one of the
            value must be non-zero. The Nth index corresponds to the N+1st dim-
            ension.
        
    """
    def __init__(self, directionalCoordinates = []):
        self.directionalCoordinates = directionalCoordinates[:]
    
    def ChangeDirection(self, direction):
        """
        input:
            directionalCoordinates - list of integers
                The new set of directional coordinates to replace the old.
        output:
            none
        
        Represents a change in the direction of the direction object. Must pass
        a validity check first.
        
        """
        isValid = False
        for dirCoord in direction.directionalCoordinates:
            if (not isValid) and dirCoord != 0:
                isValid = True
            if (isValid) and dirCoord != 0:
                isValid = False
                break
        if isValid:
            self.directionalCoordinates = direction.directionalCoordinates
                
                