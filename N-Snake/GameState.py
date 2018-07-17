# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:12:31 2018

@author: Isik
"""
from Nartesian import Plane
from Snake import Snake
from Position import Position
from Food import Food
from Board import Board 
import random
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
        return self.snake.ChangeDirection(direction)
    
    def MoveSnake(self):
        self.snake.Move()
        
    def CreateFood(self):
        validPositions = list(self.board.boardPositions)
        for snakeSeg in self.snake.snakeSegments:
            if snakeSeg.position in validPositions:
                validPositions.remove(snakeSeg.position)
                
        randomPositionIndex = random.randint(0,len(validPositions) - 1)
        randomPosition = validPositions[randomPositionIndex]
        
        self.food.position = randomPosition

        
    def CheckForCollision(self):
        
        snakeHead = self.snake.snakeSegments[0]
        for snakeSegment in self.snake.snakeSegments[1:]:
            if (snakeHead.position == snakeSegment.position):
                return True
        return False

        
    def CheckForEating(self):
        
        snakeHead = self.snake.snakeSegments[0]
        return snakeHead.position == self.food.position

        
    def CalculateProjections(self):
        None

    
    def ExecuteTurn(self):
        self.MoveSnake()
        if self.CheckForCollision():
            print("YOU HAVE LOST")
            self.EndGame(False)
        if self.CheckForEating():
            print("YOU HAVE EATEN")
            self.snake.Eat()
            self.board.AddDimension()
            self.CreateFood()
            
    def EndGame(self, isWon):
        None
        #TOBEIMPLEMENTED
            
    def StartGame(self, boardSize, difficulty):
        self.board = Board(0, boardSize)
        self.boardSize = boardSize
        self.difficulty = difficulty
        
        self.snake = Snake(Position())
        self.food = Food(Position())
        self.plane = Plane()
        
        self.numberOfDimensions = 0
        self.foodEaten = 0