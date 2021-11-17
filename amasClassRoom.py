#my amas

from pyAmakCore.classes.amas import Amas
from classroom import Classroom
from light import SmartLight
from shutters import Shutters

from matplotlib import pyplot as mp
import numpy as np



class MyAmas(Amas):

    numberOfLights = 8
    numberOfShutters = 4
    numberOfSensors = 3

    global_bright = []
    
    def __init__(self,Classroom):
        super().__init__(Classroom)
        self.current_time_index = 0
        self.niv_lum()
    
    def on_initialization(self):
        print("intialized AMAS")
    
    def gaussian(self, x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

    def niv_lum(self):
         # mesure toute les 20 min (660min/20min=33) 
        x_values = np.linspace(7, 18, 33)
        for x_val in x_values:
            self.global_bright.append(self.gaussian(x_val, 12, 1.7))
        print(self.global_bright)

    def on_cycle_begin(self):
        self.__environment.set_lum(self.global_bright[self.current_time_index])

    def on_cycle_end(self):
        pass

c=Classroom(0,1)
t = MyAmas(c)
t.niv_lum()