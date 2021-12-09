
from pyAmakCore.classes.agent import Agent
from  classroom import Classroom
import time

class SmartLight(Agent):
    
    
    def __init__(self,amas,posX: float = 0,posY: float =0,niv_lum = 0):
        print("Create agent ")
        super().__init__(amas)
        print("on cycle begin Light")
        print("on perceive Light")
        self.posX = posX
        self.posY = posY
        self.current_time = 0
        self.niv_lum = 0
        self.niv_lum_pred = 0
        self.InitialLightLvl=0
        

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def on_cycle_begin(self) :
        #time.sleep(1)
        self.on_perceive()
        self.current_time+=1
        
        
    def on_cycle_end(self) -> None:
        if self.current_time==33:
            print("Agent Smart_ light Cycle is finished")

    def on_perceive(self):
        if self.current_time<34:
            self.niv_lum = Classroom.global_bright[self.current_time]
            self.niv_lum_pred = Classroom.global_bright[self.current_time-1]
            self.on_act()
        else:
            self.on_cycle_end()    

    def on_act(self):
    	#ajuster la luminosité en fonction des capteurs incluts dedans  
        if self.niv_lum<0.2 :
            print("*****************************************************************")
            print("*****************************************************************")
            print("niveau de lumiére < 20%")
            self.InitialLightLvl = 100  
            print("heure:",round(self.current_time*20/60,2)+7,"Light Level Actuel  :",self.niv_lum)
            print("Allumage des Smart Lights à 100%")
            self.niv_lum+= 30/100
            Classroom.global_bright[self.current_time] += 30/100
            print("Light Level  Aprés l'allumage des Lampes :",self.niv_lum)
            print("*****************************************************************")
            print("*****************************************************************")
        elif self.niv_lum>0.6:
            print("*****************************************************************")
            print("*****************************************************************")
            print("niveau de lumiére > 60%")
            print(self.niv_lum)
            print("Les Smart Lights sont éteintes")
            self.InitialLightLvl = 0
            Classroom.global_bright[self.current_time] -= 30/100
            self.niv_lum-= 30/100
            print("heure:",round(self.current_time*20/60,2)+7,"Light Level  :",self.niv_lum)
            print("*****************************************************************")
            print("*****************************************************************")

        else:
            print("*****************************************************************")
            ecart=self.niv_lum-self.niv_lum_pred
            print("ajustement de la luminosité ")
            if ecart>0:
                print("*****************************************************************")
                
                self.InitialLightLvl-=ecart
                Classroom.global_bright[self.current_time] -= (ecart+10)/100
                self.niv_lum-= (ecart+10)/100
                print("*****************************************************************")
                print("heure:",round(self.current_time*20/60,2)+7,"Light Level  Aprés l'allumage des Lampes :",self.niv_lum)
                print("*****************************************************************")
            else:
                self.InitialLightLvl+=ecart
                Classroom.global_bright[self.current_time] += (ecart+10)/100
                self.niv_lum+= (ecart+10)/100
                print("*****************************************************************")
                print("heure:",round(self.current_time*20/60,2)+7,"Light Level  Aprés l'allumage des Lampes :",self.niv_lum)
                print("*****************************************************************")
        self.current_time +=1

