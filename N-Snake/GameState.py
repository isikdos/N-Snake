# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:12:31 2018

@author: Isik
"""
from Nartesian import Plane
from Snake import Snake
from Position import Position
from Food import Food

class GameState:
    """
    The object that controls the game and the game rules.
    Has absolute knowledge of every object within the game, and interplays bet-
    ween them to achieve desired outcomes.
    
    ###TODO add properties
    """
    
    
    def __init__(self, boardSize, difficulty):
        self.StartGame(boardSize, difficulty)
        
        
    def SetPlane(self, axes):
        self.plane.SetAxes(axes)
    
    def ChangeSnakeDirection(self, direction):
        self.snake.ChangeDirection(direction)
    
    def MoveSnake(self):
        self.snake.Move()
        
    def CreateFood(self):
        None
        #TOBEPLIEMENTED
        
    def CheckForCollision(self):
        None
        #TOBEIMPLEMENTED
        
    def CheckForEating(self):
        None
        #TOBEIMPLEMENTED
        
    def CalculateProjections(self):
        None
        #TOBEIMPLEMENTED
    
    def StartGame(self, boardSize, difficulty):
        self.boardSize = boardSize
        self.difficulty = difficulty
        
        self.snake = Snake(Position())
        self.food = Food(Position())
        self.plane = Plane()
        
        self.numberOfDimensions = 0
        self.foodEaten = 0