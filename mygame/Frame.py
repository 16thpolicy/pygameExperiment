import pygame

class Frame():
    def __init__(self,width,height,stage_dimensions):
        self.frontpoint=[0,0]
        self.backpoint=[width,height]
        self.stage_dimensions=tuple(stage_dimensions)