# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:31:08 2018

@author: Isik
"""
from Position import Position
class Board:
    """
    A class that represents and N-board
    """
    def __init__(self, numberOfDimensions, boardSize):
        self.boardSize = boardSize
        self.boardPositions = [Position([])]
        for i in range(numberOfDimensions):
            self.AddDimension()
    
    def AddDimension(self):
        """
        Increments the number of dimensions in the board, and calculates all t-
        he new board positions.
        """
        newBoardPositions = []
        if self.boardPositions == []:
            for i in self.boardSize:
                newBoardPositions.append(Position(i))
        else:
                
            for j in self.boardPositions:
                for i in range(self.boardSize):
                    oldPos = Position(j.coordinates)
                    oldPos.coordinates.append(i)
                    newBoardPositions.append(oldPos)
        self.boardPositions = newBoardPositions
            