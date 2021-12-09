
from pyAmakCore.classes.environment import Environment
from matplotlib import pyplot as mp
import time
import numpy as np

# Notre environnement 


class Classroom(Environment):
    
    global_bright = []

    def __init__(self):
        super().__init__()
        
        # Dimension de la classroom
        #self.longueur = x
        #self.largeur = y
        
        # Init time in classroom
        self.current_time = 0
        #print("il est",self.class_time)
        
        # Init variables
        self.lum = 0
        self.on_initialization()

    def gaussian(self, x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

    def niv_lum(self):
        # mesure toute les 20 min (660min/20min=33) 
        x_values = np.linspace(7, 18, 33)
        for x_val in x_values:
            self.global_bright.append(self.gaussian(x_val, 12, 1.7))
        #print(self.global_bright)

    def on_initialization(self) -> None:
        self.niv_lum()
        self.set_lum(self.global_bright[0])
    
    def on_cycle_begin(self):

        if self.current_time < 33:
            self.set_lum(self.global_bright[self.current_time])
           # print("current_time {} ,lum {}".format(self.current_time,self.lum))
            self.current_time +=1
     
    def on_cycle_end(self):
        print("environment cycle finished")

    def set_lum(self, lum):
        self.lum = lum

    def get_lum(self):
        return self.lum   


