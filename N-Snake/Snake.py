# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:15:48 2018

@author: Isik
"""
from Direction import Direction

class Snake:
    """
    This class represents a snake itself.
    It has, most importantly, a body and a direction.
    
    This snake can exist in N dimensions, and as such can have N directions.
    
    --------------------------------------------------------------------------
    Properties
    --------------------------------------------------------------------------
    snakeSegments:      List of Snake_Segment type object
        Represents the snake's body. The 0th segment is the head and is treated
        as such, the rest of the segments follow the head traveling where it u-
        sed to be. The body is important only for the cases of collision, and
        non-trivial food spawning. 
        
    direction:          A single direction object
        Represents the snake's direction of travel. Realistically only affects
        the head
    
    segmentsToGrow:     An integer
        Represents the number of segments the snake has to grow. It will grow
        by one segment in length per turn, and the number of segments gained by
        eating food could hypothetically be variable.
    """
    def __init__(self, position, segmentsPerFood = 1):
        self.snakeSegments = [ Snake_Segment(position) ]
        self.direction = Direction()
        self.segmentsToGrow = 0
        self.segmentsPerFood = 1
        
    def ChangeDirection(self, direction):
        """
        input: 
            direction - direction type object
                Indicates the direction in which the snake's head will travel
        output:
            none
        
        Description:
            Changes the direction in which the snake's head travels. Must pass
            a validity check first.
        """
        if len(self.snakeSegments) == 1 or not (self.snakeSegments[0].position + direction == self.snakeSegments[1].position) :
            self.direction.ChangeDirection(direction) 
        
    def Move(self):
        """
        input:
            none
        output:
            none
            
        Description:
            Moves the snake's head one unit in the direction of travel, as def-
            ined by self.direction. The rest of the snake's body will move to
            where the previous segment used to be.
        
        """
        grow = self.segmentsToGrow > 0
        
        if (grow):
            self.segmentsToGrow -= 1
            lastPosition = self.snakeSegments[-1].position
            
        for index, segment in self.snakeSegments[1:]:
            segment.position = self.snakeSegments[index].position 
        
        if (grow):
            self.snakeSegments.append(Snake_Segment(lastPosition))
        
        self.snakeSegments[0].position = self.snakeSegments[0].position + self.direction
    
    def Eat(self):
        """
        input:
            none
        output:
            none
            
        Description:
            Called by the game once the snake eats some food. Causes the snake
            to grow on subsequent turns.
        """
        self.segmentsToGrow += self.segmentsPerFood

class Snake_Segment:
    """
    This class represents one segment of the snake.
    A snake is physically comprised of N segments.
    """
    
    def __init__(self, position):
        self.position = position
        