# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:27:15 2018

@author: Isik
"""


class Food:
    """
    Represents a piece of food.
    It has a position.
    It gets eaten.
    It's a snake food.
    Not that complicated, hombre.
    """
    def __init__(self, position):
        self.position = position