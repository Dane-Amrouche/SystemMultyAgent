
from pyAmakCore.classes.environment import Environment
from matplotlib import pyplot as mp
import time
import numpy as np

# Notre environnement 

class Classroom(Environment):
    def __init__(self,x,y):
        super().__init__()
        
        # Dimension de la classroom
        self.longueur = x
        self.largeur = y
        
        # Init time in classroom
        self.class_time = time.time()
        print("il est",self.class_time)
        
        # Init variables
        self.lum = 0


    def time(self):
        return time.time()

    def set_lum(self, lum):
        self.lum = lum

    def get_lum(self):
        return lum   


t = Classroom(0,0)