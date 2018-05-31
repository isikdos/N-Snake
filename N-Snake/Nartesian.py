# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:02:36 2018

@author: Isik
"""

class Plane: 
    """
    An object for representing a cartesian plane. It will describe itself acco-
    rding to two rays, and because of how the program is written it will only
    anticipate that it is a plane along two fundamental axes - aka, the x,y pl-
    ane or the y-z plane. 

    ---------------------------------------------------------------------------
    Properties
    ---------------------------------------------------------------------------
    axes:   List of up to two Ray type objects
    
    """
    def __init__(self, axes = []):
        self.axes = axes
        
    def SetAxes(self, axes):
        if len(axes) > 2:
            raise ValueError("Cannot have more than two axes at once")
        if len(axes) == 2:
            if (axes[0] == axes[1]):
                raise ValueError("Both axes cannot be in the same dimension")
        self.axes = axes

    
class Ray:
    """
    An object for representing a ray. That is to say, a vector with a start po-
    int and an end point. The start point will always be the origin, and the e-
    nd point is position number of units away from the origin.
    
    ---------------------------------------------------------------------------
    Properties
    ---------------------------------------------------------------------------
    dimension:      integer
        Represents the dimension the ray is in
        
    position:       integer
        represents the displacement from the origin along the chosen dimension.
    """
    def __init__(self, dimension, displacement):
        self.dimension = dimension
        self.displacement = displacement
        
        
    def __eq__(self, other):
        """
        Equality defintion for Ray:
            
        NOTE!!!!!!!!!!!!!!!!!!!!
        It does not care if the displacements are different, it only cares if
        dimensions are different.
        """
        if isinstance(self, other.__class__):
            return (self.axes[0].dimension == other.dimension)
        return False